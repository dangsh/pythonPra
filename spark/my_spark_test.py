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
a = rdd.take(2)[1]
import json
import pyquery
import pymongo
url = a[0]
mongo_client = pymongo.MongoClient("192.168.14.90", 27017)
db = mongo_client["test"]
def get_unicode(s):
    try:
        return '' if not s else (eval('''"%s"''' % (s.replace('"', '\\"').replace("'", "\\'")))).decode("utf-8")
    except:
        return s
content = ''
try:
    content = json.loads(a[1])["value"]
except:
    pass
if not content:
    continue
try:
    content = get_unicode(content)
except:
    pass
doc = pyquery.PyQuery(content)
if "_" in url:
    try:
        for i in doc('.relate-product .relate-list li').items():
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
else:
    try:
        for i in doc('.hotproword a').items():
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