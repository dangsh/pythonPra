# coding:utf-8
# write  by  zhou
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.rdd import RDD

sc = SparkContext(appName='hy88_product_test')

product_test_conf = {"hbase.mapreduce.inputtable": "hy88_product_test",
                     "hbase.client.scanner.timeout.period": "1000000",
                     "hbase.zookeeper.quorum": "172.20.10.11,172.20.10.207,172.20.10.68"}
test11_conf = {"hbase.mapreduce.inputtable": "test11", "hbase.client.scanner.timeout.period": "1000000",
               "hbase.zookeeper.quorum": "172.20.10.11,172.20.10.207,172.20.10.68"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
product_test_rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                                      "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                                      "org.apache.hadoop.hbase.client.Result",
                                      conf=product_test_conf, keyConverter=keyConv,
                                      valueConverter=valueConv).repartition(20)

test11_rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                                "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                                "org.apache.hadoop.hbase.client.Result",
                                conf=test11_conf, keyConverter=keyConv, valueConverter=valueConv).repartition(40)


def map_fun(data):
    import json
    def get_unicode(s):
        try:
            return '' if not s else (eval('''"%s"''' % (s.replace('"', '\\"').replace("'", "\\'")))).decode("utf-8")
        except:
            return ''

    url = data[0]
    try:
        content = get_unicode(json.loads(data[1])["value"])
    except:
        content = ''
    if content:
        try:
            info = json.loads(content)
            return (url, info)
        except:
            pass


test11_rdd = test11_rdd.map(map_fun).filter(lambda x: x != None).map(lambda x: [x[0], (x[1], "test11_rdd")])
product_test_rdd = product_test_rdd.map(map_fun).filter(lambda x: x != None).map(
    lambda x: [x[0], (x[1], "product_test_rdd")])


def reduct_fun(x, y):
    if x[1] == "test11_rdd":
        return x[0]
    if y[1] == "test11_rdd":
        return y[0]


rdd = product_test_rdd.union(test11_rdd).partitionBy(90,lambda x:x[0]).reduceByKey(reduct_fun).filter(lambda x: isinstance(x[1], dict))
rdd = rdd.repartition(40)

print rdd.count()

def map_fun_1(iter):
    import happybase
    import json
    conn = happybase.Connection("172.20.10.84", 6004)
    table = conn.table("hy88_product_test")
    for item in iter:
        key, data = item
        table.put(key, {"info:json": json.dumps(data)})


rdd.foreachPartition(map_fun_1)
