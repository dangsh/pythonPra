# coding:utf-8
__author__ = 'qinman'
# create by qinman on 2018/4/8
from pyspark.sql import SparkSession
from pyspark.rdd import  StorageLevel,portable_hash
spark = SparkSession.builder.appName('refine_hy88').getOrCreate()
sc = spark.sparkContext

conf = {"hbase.zookeeper.quorum":  "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hy88", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)

def url_func(x):
    import re
    if re.search(r'huangye88.com/xinxi/\d+\.html', x[0]) or re.search(r"huangye88.com/xinxi/\d+_\d+\.html", x[0]):
        return x


rdd = rdd.map(url_func).filter(lambda x: x != None)


rdd_1 = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri", "mongodb://192.168.14.90/zkp.huangye88_product_url").option('numberOfPartitions', 1000).load().rdd.map(lambda x: (x._id, 1))
rdd_1.persist(StorageLevel(True,False,False,False))
rdd_1.count()


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


rdd_2 = rdd.flatMap(map_func).distinct().filter(lambda x: x != None).map(lambda x: (x, 1))
rdd_2.persist(StorageLevel(True,False,False,False))
spark.createDataFrame(rdd_2, ['url',"value"]).write.format("com.mongodb.spark.sql.DefaultSource").mode("ignore").option("uri", "mongodb://192.168.14.90/final_field.refine_hy88_rdd2").save()

rdd_3 = rdd_2.union(rdd_1).countByKey().filter(lambda x: x[1] == 1)
rdd_4 = rdd_3.map(lambda x: (x[0], ))

spark.createDataFrame(rdd_4, ['url']).write.format("com.mongodb.spark.sql.DefaultSource").mode("ignore").option("uri", "mongodb://192.168.14.90/final_field.refine_hy88").save()
