# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 4 23
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('hy88_get_url').getOrCreate()
sc = spark.sparkContext

conf1 = {"hbase.zookeeper.quorum":  "172.20.10.11:2181", "hbase.mapreduce.inputtable": "hy88_company_order", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf1, keyConverter=keyConv, valueConverter=valueConv)
def map_fun(data):
    import json
    data = json.loads(data[1])
    return str(data["value"])
rdd = rdd.map(map_fun)
from pyspark.sql import Row
emp = rdd.map(lambda p : Row(url=p))
df = spark.createDataFrame(emp)
url="jdbc:mysql://192.168.14.90:3306/hy88?user=spider&password=123456"
df.write.jdbc(url=url,mode="append",table="com_url",properties={"driver":"com.mysql.jdbc.Driver"})