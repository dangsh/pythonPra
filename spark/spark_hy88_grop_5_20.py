# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 5 11
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('hy88_get_some_product ').getOrCreate()
sc = spark.sparkContext
conf = {"hbase.zookeeper.quorum":  "172.20.10.11,172.20.10.207,172.20.10.68",
        "hbase.mapreduce.inputtable": "test11", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)
conf2 = {"hbase.zookeeper.quorum":  "172.20.10.11,172.20.10.207,172.20.10.68",
        "hbase.mapreduce.inputtable": "hy88_product_test", "hbase.client.scanner.timeout.period":"1000000"}
valueConv2 = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv2 = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd2 = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf2, keyConverter=keyConv2, valueConverter=valueConv2)
def map_func(x):
    import json
    a = json.loads(x[1])
    a['from'] = 'test11'
    return x[0],a
rdd = rdd.map(map_func)
def map_func2(x):
    import json
    a = json.loads(x[1])
    a['from'] = 'product'
    return x[0],a
rdd2 = rdd2.map(map_func2)
rdd = rdd.union(rdd2)
def reduce_func(a,b):
    import json
    if a != '' and b != '':
        if json.loads(a)["from"] == 'product':
            return a
        else:
            return b
    else:
        return None
rdd = rdd.reduceByKey(reduce_func).filter(lambda x : x !=None)

def map_func3(iter_x):
    for x in iter_x:
        import happybase
        from happybase_monkey.monkey import monkey_path;monkey_path()
        conn = happybase.Connection("172.20.10.192", 6004)
        try:
            conn.table('spider_hy88_company_json').put(x[0], {'info:json': json.dumps(data)})
        except:
            try:
                conn = happybase.Connection("192.168.14.2", 9090)
                conn.table('spider_hy88_company_json').put(x[0], {'info:json': json.dumps(data)})
            except:
                pass
rdd.foreachPartition(map_func3)