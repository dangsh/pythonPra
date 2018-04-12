# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 4 10
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('hy88_field_pick_2').getOrCreate()
# sc = SparkContext(spark.sparkContext)
sc = spark.sparkContext

conf = {"hbase.zookeeper.quorum":  "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hy88", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)
def map_func(iter_x):
    import json
    import pyquery
    import pymongo
    import redis
    mongo_client = pymongo.MongoClient("192.168.14.90", 27017)
    db = mongo_client["test"]
    r=redis.Redis(host='192.168.8.88',port='6379',db=0,decode_responses=True)
    def get_unicode(s):
        try:
            return '' if not s else (eval('''"%s"''' % (s.replace('"', '\\"').replace("'", "\\'")))).decode("utf-8")
        except:
            return s
    for x in iter_x:
        content = ''
        url = ''
        base_url = ''
        try:
            content = json.loads(x[1])["value"]
            base_url = x[0]
        except:
            pass
        if not content:
            continue
        try:
            r.lpush("used_url",base_url)
        except:
            try:
                r=redis.Redis(host='192.168.8.88',port='6379',db=0,decode_responses=True)
                r.lpush("used_url",base_url)
            except:
                pass
        try:
            content = get_unicode(content)
        except:
            pass
        doc = pyquery.PyQuery(content)

        try:
            for i in doc('a').items():
                if 'product' in str(i('a').attr('href')):
                    url = i('a').attr('href')
                    try:
                        db['spark_test'].insert({'_id':url})
                    except:
                        try:
                            mongo_client = pymongo.MongoClient("192.168.14.90", 27017)
                            db = mongo_client["test"]
                            db['spark_test'].insert({'_id':url})
                        except:
                            pass
        except:
            pass


rdd.foreachPartition(map_func)