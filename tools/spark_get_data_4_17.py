# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 4 17
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('hy88_get_url').getOrCreate()
sc = spark.sparkContext

conf = {"hbase.zookeeper.quorum":  "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hy88_word", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)
def map_func(iter_x):
    import json
    import pymongo
    import redis
    from lxml import etree
    import happybase
    from happybase_monkey.monkey import monkey_path;monkey_path()
    r=redis.Redis(host='192.168.8.88',port='6379',db=1,decode_responses=True)
    def get_unicode(s):
        try:
            return '' if not s else (eval('''"%s"''' % (s.replace('"', '\\"').replace("'", "\\'")))).decode("utf-8")
        except:
            return s
    for x in iter_x:
        content = ''
        base_url = ''
        key_word = ''
        classify = ''
        likely_classify = []
        likely_word = []
        goods = []
        company = []
        try:
            content = json.loads(x[1])["value"]
            base_url = x[0]
        except:
            pass
        if not content:
            continue
        try:
            r.lpush("word_json",base_url)
        except:
            pass
        try:
            content = get_unicode(content)
            selector = etree.HTML(content)
            key_word = selector.xpath('//h1/text()')
            classify = selector.xpath('//div[@style="margin-top:10px;"]/a/text()')[1]
            for i in selector.xpath('//div[@class="relate-classify"]/ul/li/a'):
                word = i.xpath('text()')
                url = i.xpath('@href')
                likely_classify.append([word[0],url[0]])
            for i in selector.xpath('//div[@class="relate-picture"]/ul/li/a'):
                word = i.xpath('text()')
                url = i.xpath('@href')
                likely_word.append([word[0],url[0]])
            for i in selector.xpath('//div[@class="infolist"]/ul/li/div[@class="all_r"]/div/div/a'):
                word = i.xpath('@title')
                url = i.xpath('@href')
                goods.append([word[0],url[0]])
            for i in selector.xpath('//td[@class="c_name"]/a'):
                word = i.xpath('text()')
                url = i.xpath('@href')
                company.append([word[0],url[0]])
        except:
            pass
        data = {
            'key_word' : key_word ,
            'classify' : classify ,
            'likely_classify' : likely_classify ,
            'likely_word' : likely_word ,
            'goods' : goods ,
            'company' : company 
        }
        conn = happybase.Connection("192.168.14.1", 9090)
        try:
            conn.table('spider_hy88_word_json').put(x[0], {'info:json': json.dumps(data)})
        except:
            try:
                conn = happybase.Connection("192.168.14.1", 9090)
                conn.table('spider_hy88_word_json').put(x[0], {'info:json': json.dumps(data)})
            except:
                pass
rdd.foreachPartition(map_func)
