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
import json
print type(rdd.first())
s = rdd.first()
s = json.loads(s[1])
print type(s)
print s
print s["value"]
