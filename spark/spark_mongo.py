# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 4 16
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.rdd import  StorageLevel

spark = SparkSession.builder.appName('hy88_company').getOrCreate()
# sc = SparkContext(spark.sparkContext)
sc = spark.sparkContext
def map_func(x):
    import json
    return [json.loads(x)["com_url"]]
rdd = sc.textFile('/data/hy88/hy88.json')
rdd = rdd.map(map_func).filter(lambda x:x != '')
rdd = rdd.distinct()

spark.createDataFrame(rdd, ['_id']).write.format("com.mongodb.spark.sql.DefaultSource").mode("ignore").option("uri", "mongodb://192.168.14.90/hy88.spark_com_url").save()