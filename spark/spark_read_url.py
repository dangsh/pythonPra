# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 4 10
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('hy88_get_url').getOrCreate()
# sc = SparkContext(spark.sparkContext)
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
    import re
    mongo_client = pymongo.MongoClient("192.168.14.90", 27017)
    db = mongo_client["hy88"]
    r=redis.Redis(host='192.168.8.88',port='6379',db=1,decode_responses=True)
    def get_unicode(s):
        try:
            return '' if not s else (eval('''"%s"''' % (s.replace('"', '\\"').replace("'", "\\'")))).decode("utf-8")
        except:
            return s
    for x in iter_x:
        content = ''
        base_url = ''
        try:
            content = json.loads(x[1])["value"]
            base_url = x[0]
        except:
            pass
        if not content:
            continue
        try:
            r.lpush("used_url2",base_url)
        except:
            pass
        try:
            content = get_unicode(content)
        except:
            pass
        reg = 'href="(http://www.huangye88.com/product/\w+.html)\"'
        urls = re.findall(reg , content)
        for i in urls:
            try:
                db['spark_url'].insert({'_id':i})
            except:
                pass


rdd.foreachPartition(map_func)