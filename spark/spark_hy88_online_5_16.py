# coding:utf-8
# write  by  zhou
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.rdd import RDD
spark = SparkSession.builder.appName('hy88_2_json_online').getOrCreate()
# sc = SparkContext(spark.sparkContext)
sc = spark.sparkContext

conf = {"hbase.zookeeper.quorum":  "192.168.14.1:2181",
        "hbase.mapreduce.inputtable": "spider_hy88_2_json", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)


def map_fun(data):
    import json
    def get_unicode(s):
        try:
            return '' if not s else (eval('''"%s"''' % (s.replace('"', '\\"').replace("'", "\\'")))).decode("utf-8")
        except:
            return ''
    url = data[0]
    try:
        cate3_info,json_info = data[1].split("\n")
        cate3_info = get_unicode(json.loads(cate3_info)["value"])
        json_info = get_unicode(json.loads(json_info)["value"])
        info = json.loads(json_info)
        info["cate_name_3"] = cate3_info
        return url,info
    except:
        pass
rdd = rdd.map(map_fun)
def map_func2(iter_x):
    from pyquery import PyQuery as pq
    from gcpy_utils.spider.handle import data_to_online
    for x in iter_x:
        try:
            detail = x[1]["detail"]
            doc = pq(detail)
        except:
            pass
        else:
            doc.find('embed').remove()
            doc.find('script').remove()
            doc('#showMore').remove()
            detail = doc.html()
            if doc('#textMore'):
                detail = doc('#textMore').html(method='html')
            if doc('.text-more'):
                detail = doc('.text-more').html(method='html')
            x[1]["detail"] = detail
        if x:
            data_to_online("hy88_product", x[0], x[1])
        else:
            pass
rdd.foreachPartition(map_func2)