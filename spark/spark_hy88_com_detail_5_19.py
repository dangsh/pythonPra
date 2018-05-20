# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 5 20
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('hy88_com_json').getOrCreate()
sc = spark.sparkContext

conf1 = {"hbase.zookeeper.quorum": "192.168.14.1:2181", "hbase.mapreduce.inputtable": "spider_hy88_company",
        "hbase.client.scanner.timeout.period": "1000000"}
valueConv1 = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv1 = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd1 = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf1, keyConverter=keyConv1, valueConverter=valueConv1)

conf = {"hbase.zookeeper.quorum": "192.168.14.2:2181", "hbase.mapreduce.inputtable": "spider_hy88_company",
        "hbase.client.scanner.timeout.period": "1000000"}
valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat",
                         "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
                         "org.apache.hadoop.hbase.client.Result",
                         conf=conf, keyConverter=keyConv, valueConverter=valueConv)
rdd = rdd.union(rdd1)
def map_func(iter_x):
    import json
    import hashlib
    import urlparse
    import collections
    import re
    from lxml import etree
    from celery.app import Celery
    import happybase
    from happybase_monkey.monkey import monkey_path;
    monkey_path()
    from gcpy_utils.spider.handle import image_to_upyun, data_to_online
    app = Celery(broker="redis://192.168.8.185:6379/6")
    app.conf.task_queue_max_priority = 255
    app.conf.task_ignore_result = True
    def get_unicode(s):
        try:
            return '' if not s else (eval('''"%s"''' % (s.replace('"', '\\"').replace("'", "\\'")))).decode("utf-8")
        except:
            return s
    for x in iter_x:
        content = ""
        base_url = ""
        comname = ""
        comname_short = ""
        com_auth = ""
        comtype = ""
        product = ""
        com_addr1 = ""
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
        com_pic_upyun = ""
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
        com_addr2 = ""
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
        try:
            try:
                content = json.loads(x[1])["value"]
                base_url = x[0]
            except:
                pass
            if not content:
                continue
            try:
                content = get_unicode(content)
                selector = etree.HTML(content)
            except:
                pass
            try:
                comname = selector.xpath('//ul[@class="l-txt"][1]/li[1]/text()')[0]
                comname_short = selector.xpath('//ul[@class="l-txt"][1]/li[2]/text()')[0]
                com_auth = selector.xpath('//div[@class="iprz five rzcom"]/text()')[0]
            except:
                pass
            for i in selector.xpath('//ul[@class="l-txt"][2]/li'):
                data = i.xpath('text()')[0]
                try:
                    if u'企业类型' in data:
                        data = data.encode('utf-8')
                        comtype = data.split('：')[1]
                        comtype = comtype.decode('utf-8')
                    if u'主营产品' in data:
                        product = i.xpath('string(.)')
                        product = product.encode('utf-8')
                        product = product.replace('主营产品：', '')
                        product = product.decode('utf-8')
                    if u'公司地址' in data:
                        com_addr1 = i.xpath('string(.)')
                        com_addr1 = com_addr1.encode('utf-8')
                        com_addr1 = com_addr1.replace('公司地址：', '')
                        com_addr1 = com_addr1.decode('utf-8')
                except:
                    pass
            for i in selector.xpath('//ul[@class="con-txt"]/li'):
                data = i.xpath('string(.)')
                try:
                    if u'企业法人' in data:
                        ceo = i.xpath('text()')[0]
                    if u'所在地' in data:
                        provinces_and_cities = i.xpath('text()')[0]
                    if u'企业类型' in data:
                        comtype = i.xpath('text()')[0]
                    if u'成立时间' in data:
                        regyear = i.xpath('text()')[0]
                    if u'注册资金' in data:
                        regcapital = i.xpath('text()')[0]
                    if u'员工人数' in data:
                        employ = i.xpath('text()')[0]
                    if u'主营行业' in data:
                        main_industry = i.xpath('a/text()')[0]
                    if u'主营地区' in data:
                        main_addr = i.xpath('text()')[0]
                    if u'主营产品' in data:
                        product = i.xpath('text()')[0]
                except:
                    pass
            for i in selector.xpath('//ul[@class="l-txt none"]/li'):
                data = i.xpath('string(.)')
                if u'联系人' in data:
                    contact = i.xpath('a/text()')[0]
                if u'用户认证' in data:
                    user_auth = i.xpath('string(.)')
                    user_auth = user_auth.encode('utf-8')
                    user_auth = user_auth.replace('用户认证：', '')
                    user_auth = user_auth.decode('utf-8')
                if u'最新登录' in data:
                    new_login = i.xpath('text()')[0]
                if u'电话' in data:
                    tel = i.xpath('text()')[0]
                if u'手机' in data:
                    mobile = i.xpath('text()')[0]
                if u'微信号' in data:
                    wechat = i.xpath('text()')[0]
            try:
                for i in selector.xpath('//div[@class="r-content"]/p[@class="txt"]'):
                    comdesc = i.xpath('string(.)')
                com_pic = selector.xpath('//span[@class="pic"]/img/@src')[0]
            except:
                pass
            for i in selector.xpath('//td'):
                data = i.xpath('string(.)')
                try:
                    if u'采购产品' in data:
                        buy_goods = i.xpath('text()')[0]
                    if u'主营地区' in data:
                        main_addr = i.xpath('text()')[0]
                    if u'研发部门人数' in data:
                        rdnum = i.xpath('text()')[0]
                    if u'经营模式' in data:
                        busmode = i.xpath('text()')[0]
                    if u'经营期限' in data:
                        period = i.xpath('text()')[0]
                    if u'最近年检时间' in data:
                        survey = i.xpath('text()')[0]
                    if u'登记机关' in data:
                        regist = i.xpath('text()')[0]
                    if u'企业状态' in data:
                        com_status = i.xpath('text()')[0]
                    if u'开户银行' in data:
                        bank_type = i.xpath('text()')[0]
                    if u'银行账号' in data:
                        bank_num = i.xpath('text()')[0]
                    if u'开户人' in data:
                        bank_people = i.xpath('text()')[0]
                    if u'品牌名称' in data:
                        brand_name = i.xpath('text()')[0]
                    if u'主要客户群' in data:
                        customer = i.xpath('text()')[0]
                    if u'年营业额' in data:
                        annulsale = i.xpath('text()')[0]
                    if u'年营出口额' in data:
                        annulexport = i.xpath('text()')[0]
                    if u'年营进口额' in data:
                        annulimport = i.xpath('text()')[0]
                    if u'经营范围' in data:
                        business = i.xpath('font/text()')[0]
                    if u'厂房面积' in data:
                        com_area = i.xpath('text()')[0]
                    if u'月产量' in data:
                        monthly_production = i.xpath('text()')[0]
                    if u'是否提供OEM' in data:
                        OEM = i.xpath('text()')[0]
                    if u'公司邮编' in data:
                        zip = i.xpath('text()')[0]
                    if u'公司电话' in data:
                        com_tel = i.xpath('text()')[0]
                    if u'公司传真' in data:
                        fax = i.xpath('text()')[0]
                    if u'公司邮箱' in data:
                        email = i.xpath('text()')[0]
                    if u'公司网站' in data:
                        website = i.xpath('text()')[0]
                    if u'行政区域' in data:
                        aministration_area = i.xpath('text()')[0]
                    if u'公司地址' in data:
                        com_addr2 = i.xpath('text()')[0]
                    if u'质量控制' in data:
                        qc = i.xpath('text()')[0]
                    if u'主要经营地点' in data:
                        address = i.xpath('text()')[0]
                    if u'公司所在地' in data:
                        com_location = i.xpath('text()')[0]
                    if u'公司注册地址' in data:
                        com_reg_addr = i.xpath('text()')[0]
                    if u'工商注册号' in data:
                        business_num = i.xpath('text()')[0]
                    if u'税务登记证号' in data:
                        tax_num = i.xpath('text()')[0]
                    if u'企业类型' in data:
                        comtype = i.xpath('text()')[0]
                    if u'注册资金' in data:
                        regcapital = i.xpath('text()')[0]
                    if u'成立时间' in data:
                        regyear = i.xpath('text()')[0]
                    if u'员工人数' in data:
                        employ = i.xpath('text()')[0]
                    if u'管理体系' in data:
                        management_system = i.xpath('text()')[0]
                    if u'联系人性别' in data:
                        conn_peopel_sex = i.xpath('text()')[0]
                    if u'联系人部门' in data:
                        conn_peopel_department = i.xpath('text()')[0]
                    if u'联系人职位' in data:
                        conn_peopel_position = i.xpath('text()')[0]
                except:
                    pass
        except:
            pass
        # 当企业页面为钻石VIP，等特殊页面时
        try:
            if not selector.xpath('//div[@class="w-layer"]'):
                try:
                    for i in selector.xpath('//div[@class="card-text mt5"]'):
                        comname = i.xpath('p[1]/text()')[0]
                        contact = i.xpath('p[2]/text()')[0]
                        mobile = i.xpath('p[3]/text()')[0]
                        tel = i.xpath('p[4]/text()')[0]
                    com_pic = selector.xpath('//div[@class="text-image"]/img/@src')[0]
                    comdesc = selector.xpath('//div[@class="pro-text"]/p/text()')[0]
                    for i in selector.xpath('//td'):
                        data = i.xpath('string(.)')
                        try:
                            if u'公司主营：' in data:
                                product = i.xpath('text()')[0]
                            if u'主营行业：' in data:
                                main_industry = i.xpath('a/text()')[0]
                            if u'采购产品：' in data:
                                buy_goods = i.xpath('text()')[0]
                            if u'主营地区：' in data:
                                main_addr = i.xpath('text()')[0]
                            if u'研发部门人数：' in data:
                                rdnum = i.xpath('text()')[0]
                            if u'经营模式：' in data:
                                busmode = i.xpath('text()')[0]
                            if u'经营期限：' in data:
                                period = i.xpath('text()')[0]
                            if u'最近年检时间：' in data:
                                survey = i.xpath('text()')[0]
                            if u'登记机关：' in data:
                                regist = i.xpath('text()')[0]
                            if u'企业状态：' in data:
                                com_status = i.xpath('text()')[0]
                            if u'开户银行：' in data:
                                bank_type = i.xpath('text()')[0]
                            if u'银行账号：' in data:
                                bank_num = i.xpath('text()')[0]
                            if u'开户人：' in data:
                                bank_people = i.xpath('text()')[0]
                            if u'品牌名称：' in data:
                                brand_name = i.xpath('text()')[0]
                            if u'主要客户群：' in data:
                                customer = i.xpath('text()')[0]
                            if u'年营业额：' in data:
                                annulsale = i.xpath('text()')[0]
                            if u'年营出口额：' in data:
                                annulexport = i.xpath('text()')[0]
                            if u'年营进口额：' in data:
                                annulimport = i.xpath('text()')[0]
                            if u'经营范围：' in data:
                                business = i.xpath('text()')[0]
                            if u'厂房面积：' in data:
                                com_area = i.xpath('text()')[0]
                            if u'月产量：' in data:
                                monthly_production = i.xpath('text()')[0]
                            if u'是否提供OEM：' in data:
                                OEM = i.xpath('text()')[0]
                            if u'公司邮编：' in data:
                                zip = i.xpath('text()')[0]
                            if u'公司电话：' in data:
                                com_tel = i.xpath('text()')[0]
                            if u'公司传真：' in data:
                                fax = i.xpath('text()')[0]
                            if u'公司邮箱：' in data:
                                email = i.xpath('text()')[0]
                            if u'公司网站：' in data:
                                website = i.xpath('text()')[0]
                            if u'行政区域：' in data:
                                aministration_area = i.xpath('text()')[0]
                            if u'公司地址：' in data:
                                com_addr2 = i.xpath('text()')[0]
                            if u'质量控制：' in data:
                                qc = i.xpath('text()')[0]
                            if u'主要经营地点：' in data:
                                address = i.xpath('text()')[0]
                            if u'公司所在地：' in data:
                                com_location = i.xpath('text()')[0]
                            if u'公司注册地址：' in data:
                                com_reg_addr = i.xpath('text()')[0]
                            if u'工商注册号：' in data:
                                business_num = i.xpath('text()')[0]
                            if u'税务登记证号：' in data:
                                tax_num = i.xpath('text()')[0]
                            if u'企业类型：' in data:
                                comtype = i.xpath('text()')[0]
                            if u'注册资金：' in data:
                                regcapital = i.xpath('text()')[0]
                            if u'成立时间：' in data:
                                regyear = i.xpath('text()')[0]
                            if u'员工人数：' in data:
                                employ = i.xpath('text()')[0]
                            if u'管理体系：' in data:
                                management_system = i.xpath('text()')[0]
                            if u'联系人性别：' in data:
                                conn_peopel_sex = i.xpath('text()')[0]
                            if u'联系人部门：' in data:
                                conn_peopel_department = i.xpath('text()')[0]
                            if u'联系人职位：' in data:
                                conn_peopel_position = i.xpath('text()')[0]
                        except:
                            pass
                except:
                    pass
        except:
            pass
        try:
            if com_pic:
                com_pic_upyun = image_to_upyun(base_url, com_pic)
        except:
            pass
        data = {
            'comname': comname,
            'comname_short': comname_short,
            'com_auth': com_auth,
            'comtype': comtype,
            'product': product,
            'com_addr1': com_addr1,
            'ceo': ceo,
            'provinces_and_cities': provinces_and_cities,
            'regyear': regyear,
            'regcapital': regcapital,
            'employ': employ,
            'main_industry': main_industry,
            'main_addr': main_addr,
            'contact': contact,
            'user_auth': user_auth,
            'new_login': new_login,
            'tel': tel,
            'mobile': mobile,
            'wechat': wechat,
            'comdesc': comdesc,
            'com_pic': com_pic,
            'com_pic_upyun': com_pic_upyun,
            'buy_goods': buy_goods,
            'rdnum': rdnum,
            'busmode': busmode,
            'period': period,
            'survey': survey,
            'regist': regist,
            'com_status': com_status,
            'bank_type': bank_type,
            'bank_num': bank_num,
            'bank_people': bank_people,
            'brand_name': brand_name,
            'customer': customer,
            'annulsale': annulsale,
            'annulexport': annulexport,
            'annulimport': annulimport,
            'business': business,
            'com_area': com_area,
            'monthly_production': monthly_production,
            'OEM': OEM,
            'zip': zip,
            'com_tel': com_tel,
            'fax': fax,
            'email': email,
            'website': website,
            'aministration_area': aministration_area,
            'com_addr2': com_addr2,
            'qc': qc,
            'address': address,
            'com_location': com_location,
            'com_reg_addr': com_reg_addr,
            'business_num': business_num,
            'tax_num': tax_num,
            'regcapital': regcapital,
            'management_system': management_system,
            'conn_peopel_sex': conn_peopel_sex,
            'conn_peopel_department': conn_peopel_department,
            'conn_peopel_position': conn_peopel_position,
        }
        data_to_online("hy88_company",x[0],data)
rdd.foreachPartition(map_func)

