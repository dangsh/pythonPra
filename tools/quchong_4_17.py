# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 4 17
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('quchong').getOrCreate()
# sc = SparkContext(spark.sparkContext)
sc = spark.sparkContext

rdd1 = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://192.168.14.90/hy88.spark_url").load().rdd.map(lambda x:x._id)
rdd1.cache()
rdd1.count()
conf = {"hbase.zookeeper.quorum":  "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hy88_word_index", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd2 = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv).map(lambda x:x[0])
rdd2.cache()
rdd2.count()
rdd = rdd1.subtract(rdd2)
rdd = rdd.map(lambda x: (x,))
spark.createDataFrame(rdd, ['_id']).write.format("com.mongodb.spark.sql.DefaultSource").mode("ignore").option("uri", "mongodb://192.168.14.90/hy88.quchong_url").save()