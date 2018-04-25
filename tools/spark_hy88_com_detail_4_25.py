# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 4 25
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('hy88_get_detail').getOrCreate()
sc = spark.sparkContext

conf = {"hbase.zookeeper.quorum":  "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hy88_company", "hbase.client.scanner.timeout.period":"1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)

x = rdd.first()
import json
from lxml import etree
def get_unicode(s):
    try:
        return '' if not s else (eval('''"%s"''' % (s.replace('"', '\\"').replace("'", "\\'")))).decode("utf-8")
    except:
        return s
try:
    content = json.loads(x[1])["value"]
    base_url = x[0]
except:
    pass
content = get_unicode(content)
selector = etree.HTML(content)

comname = ""
comname_short = ""
com_auth = ""
comtype = ""
product = ""
com_addr = ""
ceo = ""
provinces_and_cities = ""
comtype = ""
regyear = ""
regcapital = ""
employ = ""
main_industry = ""
main_addr = ""
product = ""
contact = ""
user_auth = ""
new_login = ""
tel = ""
mobile = ""
wechat = ""
comdesc = ""
com_pic = ""
buy_goods = ""
main_addr = ""
rdnum = ""
busmode = ""
period = ""
survey = ""
regist = ""
com_status = ""
bank_type = ""
bank_num = ""
bank_people = ""
brand_name = ""
customer = ""
annulsale = ""
annulexport = ""
annulimport = ""
business = ""
com_area = ""
monthly_production = ""
OEM = ""
zip = ""
com_tel = ""
fax = ""
email = ""
website = ""
aministration_area = ""
com_addr = ""
qc = ""
address = ""
com_location = ""
com_reg_addr = ""
business_num = ""
tax_num = ""
comtype = ""
regcapital = ""
regyear = ""
employ = ""
management_system = ""
conn_peopel_sex = ""
conn_peopel_department = ""
conn_peopel_position = ""



comname = selector.xpath('//ul[@class="l-txt"][1]/li[1]/text()')[0]
comname_short = selector.xpath('//ul[@class="l-txt"][1]/li[2]/text()')[0]
com_auth = selector.xpath('//div[@class="iprz five rzcom"]/text()')[0]
comtype = ""
for i in selector.xpath('//ul[@class="l-txt"][2]/li'):
    data = i.xpath('text()')[0]
    if u'企业类型' in data:
        data = data.encode('utf-8')
        comtype = data.split('：')[1]
        comtype = comtype.decode('utf-8')

product = ""
for i in selector.xpath('//ul[@class="l-txt"][2]/li'):
    data = i.xpath('text()')[0]
    if u'主营产品' in data:
        product = i.xpath('string(.)')
        product = product.encode('utf-8')
        product = product.replace('主营产品：','')
        product = product.decode('utf-8')

com_addr = ""
for i in selector.xpath('//ul[@class="l-txt"][2]/li'):
    data = i.xpath('text()')[0]
    if u'公司地址' in data:
        com_addr = i.xpath('string(.)')
        com_addr = com_addr.encode('utf-8')
        com_addr = com_addr.replace('公司地址：','')
        com_addr = com_addr.decode('utf-8')

ceo = ""
for i in selector.xpath('//ul[@class="con-txt"]/li'):
    data = i.xpath('string(.)')
    if u'企业法人' in data:
        ceo = i.xpath('text()')

provinces_and_cities = ""
for i in selector.xpath('//ul[@class="con-txt"]/li'):
    data = i.xpath('string(.)')
    if u'所在地' in data:
        provinces_and_cities = i.xpath('text()')

comtype = ""
for i in selector.xpath('//ul[@class="con-txt"]/li'):
    data = i.xpath('string(.)')
    if u'企业类型' in data:
        comtype = i.xpath('text()')

regyear = ""
for i in selector.xpath('//ul[@class="con-txt"]/li'):
    data = i.xpath('string(.)')
    if u'成立时间' in data:
        regyear = i.xpath('text()')

regcapital = ""
for i in selector.xpath('//ul[@class="con-txt"]/li'):
    data = i.xpath('string(.)')
    if u'注册资金' in data:
        regcapital = i.xpath('text()')

employ = ""
for i in selector.xpath('//ul[@class="con-txt"]/li'):
    data = i.xpath('string(.)')
    if u'员工人数' in data:
        employ = i.xpath('text()')

main_industry = ""
for i in selector.xpath('//ul[@class="con-txt"]/li'):
    data = i.xpath('string(.)')
    if u'主营行业' in data:
        main_industry = i.xpath('a/text()')

main_addr = ""
for i in selector.xpath('//ul[@class="con-txt"]/li'):
    data = i.xpath('string(.)')
    if u'主营地区' in data:
        main_addr = i.xpath('text()')

product = ""
for i in selector.xpath('//ul[@class="con-txt"]/li'):
    data = i.xpath('string(.)')
    if u'主营产品' in data:
        product = i.xpath('text()')

contact = ""
for i in selector.xpath('//ul[@class="l-txt none"]/li'):
    data = i.xpath('string(.)')
    if u'联系人' in data:
        contact = i.xpath('a/text()')

user_auth = ""
for i in selector.xpath('//ul[@class="l-txt none"]/li'):
    data = i.xpath('string(.)')
    if u'用户认证' in data:
        user_auth = i.xpath('string(.)')
        user_auth = user_auth.encode('utf-8')
        user_auth = user_auth.replace('用户认证：','')
        user_auth = user_auth.decode('utf-8')

new_login = ""
for i in selector.xpath('//ul[@class="l-txt none"]/li'):
    data = i.xpath('string(.)')
    if u'最新登录' in data:
        new_login = i.xpath('text()')

tel = ""
for i in selector.xpath('//ul[@class="l-txt none"]/li'):
    data = i.xpath('string(.)')
    if u'电话' in data:
        tel = i.xpath('text()')

mobile = ""
for i in selector.xpath('//ul[@class="l-txt none"]/li'):
    data = i.xpath('string(.)')
    if u'手机' in data:
        mobile = i.xpath('text()')

wechat = ""
for i in selector.xpath('//ul[@class="l-txt none"]/li'):
    data = i.xpath('string(.)')
    if u'微信号' in data:
        wechat = i.xpath('text()')

comdesc = ""
for i in selector.xpath('//div[@class="r-content"]/p[@class="txt"]'):
	comdesc = i.xpath('string(.)')


com_pic = ""
com_pic = selector.xpath('//span[@class="pic"]/img/@src')

buy_goods = ""
main_addr = ""
rdnum = ""
busmode = ""
period = ""
survey = ""
regist = ""
com_status = ""
bank_type = ""
bank_num = ""
bank_people = ""
brand_name = ""
customer = ""
annulsale = ""
annulexport = ""
annulimport = ""
business = ""
com_area = ""
monthly_production = ""
OEM = ""
zip = ""
com_tel = ""
fax = ""
email = ""
website = ""
aministration_area = ""
com_addr = ""
qc = ""
address = ""
com_location = ""
com_reg_addr = ""
business_num = ""
tax_num = ""
comtype = ""
regcapital = ""
regyear = ""
employ = ""
management_system = ""
conn_peopel_sex = ""
conn_peopel_department = ""
conn_peopel_position = ""