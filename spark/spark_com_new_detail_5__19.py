# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 5 19
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('hy88_get_detail').getOrCreate()
sc = spark.sparkContext

conf = {"hbase.zookeeper.quorum": "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hy88_company",
        "hbase.client.scanner.timeout.period": "1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)
def map_func(iter_x):
    for x in iter_x:
        return x[0]
rdd = rdd.map(map_func)
rdd = rdd.map(lambda x: (x,))
spark.createDataFrame(rdd, ['_id']).write.format("com.mongodb.spark.sql.DefaultSource").mode("ignore").option("uri", "mongodb://192.168.14.90/hy88.com_url_5_19").save()