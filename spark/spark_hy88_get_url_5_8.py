# coding:utf-8
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.rdd import  StorageLevel

spark = SparkSession.builder.appName('get_url').getOrCreate()
sc = spark.sparkContext
conf = {"hbase.zookeeper.quorum":  "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hy88_word_json", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)
def map_func0(x):
    import json
    content = ''
    data = []
    try:
        content = json.loads(x[1])["value"]
    except:
        pass
    try:
        content = eval('''"%s"''' % (content.replace('"', '\\"').replace("'", "\\'"))).decode("utf-8")
        content = json.loads(content)
    except:
        pass
    if content:
        for i in content["goods"]:
            data.append(i[1])
    return data
rdd_more = rdd.flatMap(map_func0).distinct().filter(lambda x: x != None)
rdd_more.persist(StorageLevel(True,True,False,False))
def map_func3(x):
    import json
    x = json.loads(x)
    return x['_id']
rdd1 = sc.textFile('/huangye88_product_url.json').map(map_func3)
def map_func(x):
    import json
    x = json.loads(x)
    return x['url']
rdd2 = sc.textFile('/refine_hy88.json').map(map_func)
def map_func2(x):
    import json
    x = json.loads(x)
    return x['_id']
rdd4 = sc.textFile('/url_5_2.json').map(map_func2)
def map_func5(x):
    import json
    x = json.loads(x)
    return x['_id']
rdd5 = sc.textFile('/url_5_7.json').map(map_func5)
rdd3 = rdd1.union(rdd2)
rdd3 = rdd3.union(rdd4)
rdd3 = rdd3.union(rdd5)
rdd3 = rdd3.distinct().filter(lambda x: x != None)
rdd3.persist(StorageLevel(True,True,False,False))
print rdd3.count()
final_rdd = rdd_more.subtract(rdd3)
final_rdd = final_rdd.map(lambda x: (x,))
spark.createDataFrame(final_rdd, ['_id']).write.format("com.mongodb.spark.sql.DefaultSource").mode("ignore").option("uri", "mongodb://192.168.14.90/hy88.url_5_8").save()