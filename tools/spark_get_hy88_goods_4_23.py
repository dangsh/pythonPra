# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 4 23
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('hy88_get_goods').getOrCreate()
sc = spark.sparkContext

conf1 = {"hbase.zookeeper.quorum":  "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hy88_2_index", "hbase.client.scanner.timeout.period":"1000000"}
conf2 = {"hbase.zookeeper.quorum":  "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hy88_3_index", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd1 = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf1, keyConverter=keyConv, valueConverter=valueConv)
rdd2 = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf2, keyConverter=keyConv, valueConverter=valueConv)
rdd = rdd1.union(rdd2)
rdd = rdd.map(lambda x : x[0])
def map_func(x):
    import json
    x = json.loads(x)
    return x['url']
rdd3 = sc.textFile('/python/test/refine_hy88.json')
rdd3 = rdd3.map(map_func)
final_rdd = rdd3.subtract(rdd)
final_rdd.saveAsTextFile('/python/test/myresult')