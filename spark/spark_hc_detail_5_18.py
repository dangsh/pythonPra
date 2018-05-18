# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 5 18
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('hc_get_product_detail').getOrCreate()
sc = spark.sparkContext

conf = {"hbase.zookeeper.quorum":  "192.168.14.1:2181",
        "hbase.mapreduce.inputtable": "spider_hc360", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)
def url_func(x):
    import re
    if re.search(r'.*?\.hc360.com/.*', x[0]):
        return x
rdd = rdd.map(url_func).filter(lambda x: x != None)


def get_unicode(s):
    try:
        return '' if not s else (eval('''"%s"''' % (s.replace('"', '\\"').replace("'", "\\'")))).decode("utf-8")
    except:
        return s

from lxml import etree