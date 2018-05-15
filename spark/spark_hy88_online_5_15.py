# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 5 15
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('hy88_get_product_detail').getOrCreate()
sc = spark.sparkContext

rdd1 = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://192.168.14.90/hy88.some_data").load()
def map_func(iter_x):
    from gcpy_utils.spider.handle import data_to_online
    for x in iter_x:
        _id = ""
        data = x.asDict()
        try:
            _id = data['_id']
        except:
            pass
        data_to_online("hy88_product_test", _id, data)
rdd1.foreachPartition(map_func)