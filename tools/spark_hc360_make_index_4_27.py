# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 4 27
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('make_index').getOrCreate()
sc = spark.sparkContext

conf = {"hbase.zookeeper.quorum":  "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hc360", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)

def map_func(iter_x):
    import happybase
    for x in iter_x:
        conn = happybase.Connection("192.168.14.2", 9090)
        try:
            conn.table('spider_hc360_index').put(x[0], {'info:a': ''})
        except:
            try:
                conn = happybase.Connection("192.168.14.2", 9090)
                conn.table('spider_hc360_index').put(x[0], {'info:a': ''})
            except:
                pass
rdd.foreachPartition(map_func)
