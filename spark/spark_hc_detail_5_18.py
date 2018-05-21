# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 5 18
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('hc_get_product_detail').getOrCreate()
sc = spark.sparkContext

conf = {"hbase.zookeeper.quorum":  "192.168.14.1:2181",
        "hbase.mapreduce.inputtable": "spider_hc360", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)
def url_func(x):
    import re
    if re.search(r'.*?\.hc360.com/.*', x[0]):
        return x
rdd = rdd.map(url_func).filter(lambda x: x != None)
def map_func2(iter_x):
    from lxml import etree
    import json
    from gcpy_utils.spider.handle import image_to_upyun, data_to_online
    def get_unicode(s):
        try:
            return '' if not s else (eval('''"%s"''' % (s.replace('"', '\\"').replace("'", "\\'")))).decode("utf-8")
        except:
            return s
    for x in iter_x:
        title = ""
        price = ""
        offer_num = ""
        send_time = ""
        send_money = ""
        com_name = ""
        buy_sell_num = ""
        com_addr = ""
        auth = ""
        com_url = ""
        mobile = ""
        telephone = ""
        seller = ""
        attrs_kv = []
        detail = ""
        thumb_1 = ""
        thumb_2 = ""
        thumb_3 = ""
        cate_name_1 = ""
        cate_name_2 = ""
        cate_name_3 = ""
        try:
            content,data = x[1].split('\n')
            content = json.loads(content)["value"]
            data = json.loads(data)["value"]
        except:
            pass
        if not content:
            continue
        try:
            content = get_unicode(content)
            data = get_unicode(data)
            selector_content = etree.HTML(content)
            selector_data = etree.HTML(data)
        except:
            pass
        try:
            title = selector_content.xpath('//h1[@class="proTitle"]/text()')[0]
            for i in selector_content.xpath('//div[@class="topPriceRig"]'):
                price = i.xpath('text()')[1]
            price = price.replace('\r','').replace('\n','').replace('\t','').replace(' ','')
            offer_num = selector_content.xpath('//span[@class="supply-numb"]/text()')[0]
            for i in selector_content.xpath('//div[@class="item-row-w"]'):
                row = i.xpath('string(.)')
                if u'发货期限' in row:
                    send_time = i.xpath('text()')[1]
            send_time = send_time.replace('\r','').replace('\n','').replace('\t','').replace(' ','')
            try:
                send_money = selector_content.xpath('//span[@class="i-txt"]')[0]
                com_name = selector_content.xpath('//div[@class="comply-name"]/p/a/text()')[0]
                buy_sell_num = selector_content.xpath('//li[@class="line-btm"]/div/a/text()')[0]
            except:
                pass
            for i in selector_content.xpath('//div[@class="item-mmt-txt"]/ul/li'):
                row = i.xpath('string(.)')
                if u'所在地区' in row:
                    com_addr = i.xpath('div/p/text()')[0]
                if u'认证信息' in row:
                    try:
                        auth = i.xpath('div/a/text()')[0]
                    except:
                        auth = i.xpath('div/text()')[0]
            com_url = selector_content.xpath('//p[@class="cName"]/a/@href')[0]
            mobile = selector_content.xpath('//em[@class="c-red"]/text()')[0][1:]
            telephone = selector_content.xpath('//div[@class="p tel1"]/em/text()')[0]
            telephone = telephone[1:].split(' ')[0]
            seller = selector_content.xpath('//div[@class="p name"]/em/text()')[0][1:]
            for i in selector_content.xpath('//div[@id="pdetail"]/div/table/tr'):
                key = i.xpath('th/text()')[0].replace('\r','').replace('\n','').replace('\t','').replace(' ','')[:-1]
                value = i.xpath('td/div/p/text()')[0].replace('\r','').replace('\n','').replace('\t','').replace(' ','')
                str = key + '|' + value
                attrs_kv.append(str)
            detail = json.loads(data[1:-1])["html"]
        except:
            pass
        try:
            if com_pic:
                com_pic_upyun = image_to_upyun(base_url, com_pic)
        except:
            pass
        data = {
            'title' : title ,
            'price' : price ,
            'offer_num' : offer_num ,
            'send_time' : send_time ,
            'send_money' : send_money ,
            'com_name' : com_name ,
            'buy_sell_num' : buy_sell_num ,
            'com_addr' : com_addr ,
            'auth' : auth ,
            'com_url' : com_url ,
            'mobile' : mobile ,
            'telephone' : telephone ,
            'seller' : seller ,
            'attrs_kv' : attrs_kv ,
            'detail' : detail ,
            'thumb_1' : thumb_1 ,
            'thumb_2' : thumb_2 ,
            'thumb_3' : thumb_3 ,
            'cate_name_1' : cate_name_1 ,
            'cate_name_2' : cate_name_2 ,
            'cate_name_3' : cate_name_3 ,
        }
        data_to_online("hy88_company",x[0],data)

rdd.foreachPartition(map_func)