# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 5 2
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('get_url').getOrCreate()
sc = spark.sparkContext
conf = {"hbase.zookeeper.quorum":  "192.168.14.2:2181", "hbase.mapreduce.inputtable": "spider_hy88_zxg", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)
def map_func(x):
    import json
    import re
    content = ''
    try:
        content = json.loads(x[1])["value"]
    except:
        pass
    try:
        content = eval('''"%s"''' % (content.replace('"', '\\"').replace("'", "\\'"))).decode("utf-8")
    except:
        pass
    if content:
        tt = re.findall(r"//\w+?\.huangye88.com/xinxi/\d+_?\d+\.html",content)
        res = set()
        for i in tt:
            res.add("http:"+i)
        return  list(res)
    else:
        return []
rdd_more = rdd.flatMap(map_func).filter(lambda x: x != None)
rdd_more = rdd_more.distinct()
rdd1 = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://192.168.14.90/zkp.huangye88_product_url").load().rdd.map(lambda x:x._id)
rdd2 = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://192.168.14.90/final_field.refine_hy88").load().rdd.map(lambda x:x.url)
rdd3 = rdd1.union(rdd2)
rdd3 = rdd3.filter(lambda x: x != None).distinct()
final_rdd = rdd_more.subtract(rdd3)
final_rdd = final_rdd.map(lambda x: (x,))
spark.createDataFrame(final_rdd, ['_id']).write.format("com.mongodb.spark.sql.DefaultSource").mode("ignore").option("uri", "mongodb://192.168.14.90/hy88.url_5_2").save()