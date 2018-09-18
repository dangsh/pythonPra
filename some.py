# -*- coding: utf-8 -*-

import re
import redis
import time
import requests
import json
import datetime
import urllib2
import urllib
import pyquery
from gcpy_utils.upyun import *
import hashlib
import urlparse


class HgfSpider(RedisCrawlSpider):
    name = 'hgf'
    redis_key = 'goods_url'

    def parse(self, response):
        print(response.url)
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
        thumb = ""
        cate_name_1 = ""
        cate_name_2 = ""
        cate_name_3 = ""
        min_price = max_price = 0
        price_unit = ''
        content = data = ''
        if response.xpath('//h1[@class="proTitle"]/text()'):
            try:


                try:
                    thumb = response.xpath('//ul[@id="thumblist"]/li[1]/div/a/@rel').extract()[0]
                    thumb = re.findall(r"largeimage: '(.*?)'", thumb)[0]
                    thumb_1 = response.xpath('//ul[@id="thumblist"]/li[2]/div/a/@rel').extract()[0]
                    thumb_1 = re.findall(r"largeimage: '(.*?)'", thumb_1)[0]
                    thumb_2 = response.xpath('//ul[@id="thumblist"]/li[3]/div/a/@rel').extract()[0]
                    thumb_2 = re.findall(r"largeimage: '(.*?)'", thumb_2)[0]
                except:
                    pass
               

ss = response.xpath('//script/text()').extract()
update_time = ''
keys = []
for i in ss:
    text = i
    for j in text.split('var'):
        keys.append(j.strip())
for i in keys:
    i = i.replace('null', 'None').replace('false', 'False').replace('true', 'True')
    if i:
        try:
            exec i in locals()
        except  Exception as e:
            pass


        try:
            detail = supplyInfoJson['introduce']
            detail = detail.decode("utf-8")
        except:
            pass
        if  u'质量保证，欢迎咨询洽谈' in detail:
            my_doc = pyquery.PyQuery(response.text)
            my_doc = my_doc("#introduce")
            detail = my_doc.outer_html()
        if detail:
            try:
                doc = pyquery.PyQuery(detail)
            except:
                pass
            else:
                try:
for i in doc('img').items():
    src = i.attr('src')
    if 'hc360' not in src or 'no_pic' in src or 'nopic' in src:
        i.remove()
        continue
    if thumb and 'no_pic' in thumb:
        thumb = src
    hl = hashlib.md5()
    hl.update(src.encode(encoding='utf-8'))
    src_md5 = hl.hexdigest()  # md5加密的文件名
    # 取出图片后缀
    b = src.split(".")
    tail = b[-1]
    full_name = src_md5 + "." + tail
    
    new_src = urlparse.urljoin(response.url,src)
    pic_byte = get_pic_byte(new_src , 10)
    if not pic_byte:
        i.remove()
        continue
    upyun_pic = my_up_upyun("/" + full_name, pic_byte , 10)
    print(upyun_pic)
    i.attr('src', upyun_pic)
                except:
                    pass
                else:
                    try:
                        for i in doc('a').items():
                            if 'b2b.hc360.com/supplyself/' in i.attr('href'):
                                i.replace_with(pyquery.PyQuery(i.text()))
                    except:
                        pass
                    else:
                        detail = doc.outer_html()
            detail = detail.replace('<div style="overflow:hidden;">', '<div>')

        try:
            min_amount = int(
                response.xpath('//tr[@class="item-cur-tab"]/td/text()').extract()[0].split('-')[0].strip())
        except:
            min_amount = 1
        try:
            price = re.search(r'\d+\.?\d+', price).group()
        except:
            price = 0
        if not min_price:
            min_price = price
        if not max_price:
            max_price = price
        if offer_num:
            try:
                res = re.search(r'(\d+)(.+)', offer_num.replace(' ', '')).groups()
                offer_num = res[0]
                if len(res) > 1:
                    price_unit = res[1]
            except:
                pass

        if thumb:
            try:
hl = hashlib.md5()
hl.update(thumb.encode(encoding='utf-8'))
src_md5 = hl.hexdigest()  # md5加密的文件名
# 取出图片后缀
b = thumb.split(".")
tail = b[-1]
full_name = src_md5 + "." + tail
pic_byte = urllib2.urlopen("http:" + thumb).read()
for j in range(10):
    try:
        thumb = up_to_upyun("/" + full_name, pic_byte)
        break
    except:
        pass
            except:
                pass
        if thumb_1:
            try:
                hl = hashlib.md5()
                hl.update(thumb_1.encode(encoding='utf-8'))
                src_md5 = hl.hexdigest()  # md5加密的文件名
                # 取出图片后缀
                b = thumb_1.split(".")
                tail = b[-1]
                full_name = src_md5 + "." + tail
                pic_byte = urllib2.urlopen("http:" + thumb_1).read()
                thumb_1 = up_to_upyun("/" + full_name, pic_byte)
            except:
                pass
        if thumb_2:
            try:
                hl = hashlib.md5()
                hl.update(thumb_2.encode(encoding='utf-8'))
                src_md5 = hl.hexdigest()  # md5加密的文件名
                # 取出图片后缀
                b = thumb_2.split(".")
                tail = b[-1]
                full_name = src_md5 + "." + tail
                pic_byte = urllib2.urlopen("http:" + thumb_2).read()
                thumb_2 = up_to_upyun("/" + full_name, pic_byte)
            except:
                pass
        goods_data = {
            'source_url': response.url,
            'title': title,
            'price': price,
            'offer_num': offer_num,
            'send_time': send_time,
            'send_money': send_money,
            'com_name': com_name,
            'com_addr': com_addr,
            'auth': auth,
            'com_url': com_url,
            'mobile': mobile,
            'telephone': telephone,
            'seller': seller,
            'attrs_kv': attrs_kv,
            'detail': detail,
            'thumb_1': thumb_1,
            'thumb_2': thumb_2,
            'thumb': thumb,
            'cate_name_1': cate_name_1,
            'cate_name_2': cate_name_2,
            'cate_name_3': cate_name_3,
            'update_time': datetime.datetime.now().strftime('%Y-%m-%d'),
            'com_username': com_username,
            'keywords': keywords,
            'min_amount': min_amount,
            'min_price': min_price,
            'max_price': max_price,
            'price_unit': price_unit,
            'brand': brand,
            'to_area': to_area,
            'from_area': from_area,
            'qq': qq,
            'ww': ww,
            'fax': fax,
            'wechat': wechat,
        }

        # 获取企业url判断企业是否已被爬取
        com_url = ""
        try:
            com_url = response.xpath('//p[@class="cName"]/a/@href').extract()[0]
        except:
            pass
        if not com_url:
            try:
                com_url = response.xpath('//div[@class="goods-tit goods-tit-blue"]/a/@href').extract()[0]
            except:
                pass
        # 取出企业的关键词
        reg = 'http://(.*?).b2b.hc360.com'
        com_word = re.findall(reg, com_url)[0]
        test_com_url = 'http://spiderhub.gongchang.com/write_to_online/data_show_onerow?secret=gc7232275&dataset=hc360_company&hkey=http://' + com_word + '.wx.hc360.com/shop/show.html'
        response = requests.get(test_com_url)
        # print(response.text)
        response = json.loads(response.text)
        # False则该企业未被爬取，True则该企业已被爬取
        print(com_url, response["status"])
        if response["status"] != True:
            # 爬取该企业的信息,并将企业信息放入Item 的 com_data中，与goods_data 一起交给mongoPipe处理
            url_1 = "http://detail.b2b.hc360.com/detail/turbine/template/moblie,vmoblie,getcontact_us.html?username="
            try:
                yield scrapy.Request(url=url_1 + com_word, meta={"goods_data": goods_data, "com_word": com_word},callback=self.parse_company)
            except:
                pass
        else:
            Item = HuicongGoodsFenbuItem()
            Item["goods_data"] = goods_data
            Item["com_data"] = ""
            yield Item

    def parse_company(self, response):
        goods_data = response.meta["goods_data"]
        com_word = response.meta["com_word"]
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(response.url)
        content_1 = response.text
        try:
            content_1 = json.loads(content_1)
        except:
            content_1 = {}

        address = content_1.get('address', '')
        product = content_1.get('business', '')
        comname = content_1.get('companyName', '')
        com_auth = u'已认证' if content_1.get('isAuth', '').lower() == 'true' else u'未认证'
        contact = content_1.get('name', '')
        conn_peopel_sex = content_1.get('gender', '')
        phone_info = content_1.get('phone')
        fax = ''
        mobile = ''
        tel = ''
        if phone_info:
            for i in phone_info:
                if i['name'] == u'传真':
                    fax = i.get('value', '')
                if i['name'] == u'手机':
                    mobile = i.get('value', '')
                if i['name'] == u'电话1':
                    tel = i.get('value', '')
        conn_peopel_position = content_1.get('position', '')
        if not comname.replace(" ", ""):
            comname = u"个人用户"
        com_data = {
            'address': address,
            'product': product,
            'comname': comname,
            'com_auth': com_auth,
            'contact': contact,
            'conn_peopel_sex': conn_peopel_sex,
            'fax': fax,
            'mobile': mobile,
            'tel': tel,
            'conn_peopel_position': conn_peopel_position,
        }

        com_data["source_url"] = ''
        com_data["comname_short"] = ''
        com_data["comtype"] = ''
        com_data["com_addr1"] = ''
        com_data["ceo"] = ''
        com_data["provinces_and_cities"] = ''
        com_data["regyear"] = ''
        com_data["regcapital"] = ''
        com_data["employ"] = ''
        com_data["main_industry"] = ''
        com_data["main_addr"] = ''
        com_data["user_auth"] = ''
        com_data["new_login"] = ''
        com_data["wechat"] = ''
        com_data["comdesc"] = ''
        com_data["com_pic"] = ''
        com_data["com_pic_upyun"] = ''
        com_data["buy_goods"] = ''
        com_data["rdnum"] = ''
        com_data["busmode"] = ''
        com_data["period"] = ''
        com_data["survey"] = ''
        com_data["regist"] = ''
        com_data["com_status"] = ''
        com_data["bank_type"] = ''
        com_data["bank_num"] = ''
        com_data["bank_people"] = ''
        com_data["brand_name"] = ''
        com_data["customer"] = ''
        com_data["annulsale"] = ''
        com_data["annulexport"] = ''
        com_data["annulimport"] = ''
        com_data["business"] = ''
        com_data["com_area"] = ''
        com_data["monthly_production"] = ''
        com_data["OEM"] = ''
        com_data["zip"] = ''
        com_data["com_tel"] = ''
        com_data["email"] = ''
        com_data["website"] = ''
        com_data["aministration_area"] = ''
        com_data["com_addr2"] = ''
        com_data["qc"] = ''
        com_data["com_location"] = ''
        com_data["com_reg_addr"] = ''
        com_data["business_num"] = ''
        com_data["tax_num"] = ''
        com_data["management_system"] = ''
        com_data["conn_peopel_department"] = ''

        url_2 = 'http://detail.b2b.hc360.com/detail/turbine/template/moblie,vmoblie,getcompany_introduction.html?username='
        try:
            yield scrapy.Request(url=url_2 + com_word,
                                 meta={"goods_data": goods_data, "com_word": com_word, "com_data": com_data},
                                 callback=self.parse_company2)
        except:
            pass

    def parse_company2(self, response):
        goods_data = response.meta["goods_data"]
        com_word = response.meta["com_word"]
        com_data = response.meta["com_data"]
        print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        print(response.url)
        content_2 = response.text
        try:
            content_2 = json.loads(content_2)
        except:
            content_2 = {}
        basic_info = content_2.get('basicInfo', {})
        comdesc = basic_info.get('companyIntroduce', '')
        imageUrl = basic_info.get('imageUrl', [])
        com_pic_upyun = ""
        com_pic = ""
        if imageUrl:
            com_pic = imageUrl[0].get('companyPicUrl', '')
            if com_pic:
                # com_pic_upyun = async_image_push.image_push(x[0], com_pic)
                hl = hashlib.md5()
                hl.update(com_pic.encode(encoding='utf-8'))
                src_md5 = hl.hexdigest()  # md5加密的文件名
                # 取出图片后缀
                b = com_pic.split(".")
                tail = b[-1]
                full_name = src_md5 + "." + tail
                pic_byte = urllib2.urlopen("http:" + com_pic).read()
                com_pic_upyun = up_to_upyun("/" + full_name, pic_byte)
        detail_info = content_2.get('detailInfo', {})
        if detail_info:
            if not com_data["address"]:
                com_data["address"] = detail_info.get('address', '')
            regcapital = detail_info.get('capital', '')
            if not com_data["contact"]:
                com_data["contact"] = detail_info.get('contactPeople', '')
            regyear = detail_info.get('createDate', '')
            if not com_data["conn_peopel_sex"]:
                com_data["conn_peopel_sex"] = detail_info.get('gender', '')
            main_industry = detail_info.get('industry', '')
            if not com_data["product"]:
                com_data["product"] = detail_info.get('majorProducts', '')
            busmode = detail_info.get('pattern', '')
            phone_info = detail_info.get('phone', [])
            if phone_info:
                for i in phone_info:
                    if i['name'] == u'传真' and not com_data["fax"]:
                        com_data["fax"] = i.get('value', '')
                    if i['name'] == u'手机' and not com_data["mobile"]:
                        com_data["mobile"] = i.get('value', '')
                    if i['name'] == u'电话1' and not com_data["tel"]:
                        com_data["tel"] = i.get('value', '')
            if not com_data["conn_peopel_position"]:
                com_data["conn_peopel_position"] = detail_info.get('position', '')
            ceo = detail_info.get('representative', '')
        com_data["comdesc"] = comdesc
        com_data["com_pic"] = com_pic
        com_data["com_pic_upyun"] = com_pic_upyun
        com_data["regcapital"] = regcapital
        com_data["regyear"] = regyear
        com_data["main_industry"] = main_industry
        com_data["busmode"] = busmode
        com_data["ceo"] = ceo

        try:
            yield scrapy.Request(url='https://js.hc360.com/b2b/%s/company.html' % (com_word,),
                                 meta={"goods_data": goods_data, "com_word": com_word, "com_data": com_data},
                                 callback=self.parse_company3)
        except:
            pass

    def parse_company3(self, response):
        goods_data = response.meta["goods_data"]
        com_word = response.meta["com_word"]
        com_data = response.meta["com_data"]
        print("zzzzzzzzzzzzzzzzzzz")
        print(response.url)
        content_js = response.text
        doc = pyquery.PyQuery(content_js)
        aa = doc('article.intro-list ul')
        for i in aa('li').items():
            if i('.c-left').text() == u'主营产品或服务' and not com_data["product"]:
                com_data["product"] = i('.c-right').text()
            if i('.c-left').text() == u'主营行业' and not com_data["main_industry"]:
                com_data["main_industry"] = i('.c-right').text()
            if i('.c-left').text() == u'企业类型':
                com_data["comtype"] = i('.c-right').text()
            if i('.c-left').text() == u'经营模式' and not com_data["busmode"]:
                com_data["busmode"] = i('.c-right').text()
            if i('.c-left').text() == u'注册地址':
                com_data["com_reg_addr"] = i('.c-right').text()
            if i('.c-left').text() == u'经营地址' and not com_data["address"]:
                com_data["address"] = i('.c-right').text()
            if i('.c-left').text() == u'公司成立时间' and not com_data["regyear"]:
                com_data["regyear"] = i('.c-right').text()
            if i('.c-left').text() == u'法定代表人/负责人' and not com_data["ceo"]:
                com_data["ceo"] = i('.c-right').text()
            if i('.c-left').text() == u'员工人数':
                com_data["employ"] = i('.c-right').text()
            if i('.c-left').text() == u'年营业额':
                com_data["annulsale"] = i('.c-right').text()
            if i('.c-left').text() == u'经营品牌':
                com_data["brand_name"] = i('.c-right').text()
            if i('.c-left').text() == u'注册资本' and not com_data["regcapital"]:
                com_data["regcapital"] = i('.c-right').text()
            if i('.c-left').text() == u'主要客户群':
                com_data["customer"] = i('.c-right').text()
            if i('.c-left').text() == u'主要市场':
                com_data["main_addr"] = i('.c-right').text()
            if i('.c-left').text() == u'是否提供OEM服务':
                com_data["OEM"] = i('.c-right').text()
            if i('.c-left').text() == u'研发部门人数':
                com_data["rdnum"] = i('.c-right').text()
            if i('.c-left').text() == u'厂房面积':
                com_data["com_area"] = i('.c-right').text()
            if i('.c-left').text() == u'质量控制':
                com_data["qc"] = i('.c-right').text()
            if i('.c-left').text() == u'管理体系认证':
                com_data["management_system"] = i('.c-right').text()
            if i('.c-left').text() == u'认证信息' and not com_data["com_auth"]:
                com_data["com_auth"] = i('.c-right').text()
            if i('.c-left').text() == u'开户银行':
                com_data["bank_type"] = i('.c-right').text()
        if 'null' in com_data["regcapital"]:
            com_data["regcapital"] = u'无需验资'
        com_data["source_url"] = 'http://' + com_word + '.wx.hc360.com/shop/show.html'
        # com_data["_id"] = 'http://'+ com_word +'.wx.hc360.com/shop/show.html'

        # print(com_data)
        Item = HuicongGoodsFenbuItem()
        Item["com_data"] = com_data
        Item["goods_data"] = goods_data
        yield Item




for i in doc('img').items():
    src = i.attr('src')
    if 'hc360' not in src or 'no_pic' in src or 'nopic' in src:
        i.remove()
        continue
    if thumb and 'no_pic' in thumb:
        thumb = src
    if thumb and 'nopic' in thumb:
        thumb = src
    hl = hashlib.md5()
    hl.update(src.encode(encoding='utf-8'))
    src_md5 = hl.hexdigest()  # md5加密的文件名
    # 取出图片后缀
    b = src.split(".")
    tail = b[-1]
    full_name = src_md5 + "." + tail
    new_src = urlparse.urljoin(response.url,src)
    pic_byte = get_pic_byte(new_src, 10)
    if not pic_byte:
        i.remove()
        continue
    upyun_pic = my_up_upyun("/" + full_name, pic_byte, 10)
    i.attr('src', upyun_pic)




for i in doc('img').items():
    src = i.attr('src')
    try:
        if 'hc360' not in src or 'no_pic' in src or 'nopic' in src:
            i.remove()
            continue
    except:
        pass
    try:
        if thumb and 'no_pic' in thumb:
            thumb = src
        if thumb and 'nopic' in thumb:
            thumb = src
    except:
        pass
    hl = hashlib.md5()
    hl.update(src.encode(encoding='utf-8'))
    src_md5 = hl.hexdigest()  # md5加密的文件名
    # 取出图片后缀
    b = src.split(".")
    tail = b[-1]
    full_name = src_md5 + "." + tail
    new_src = urlparse.urljoin(response.url,src)
    pic_byte = get_pic_byte(new_src, 10)
    if not pic_byte:
        i.remove()
        continue
    upyun_pic = my_up_upyun("/" + full_name, pic_byte, 10)
    if 'hc360' in upyun_pic:
        i.remove()
        continue
    print upyun_pic
    i.attr('src', upyun_pic)    