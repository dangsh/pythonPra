# -*- coding: utf-8 -*-
import requests
from pymongo import MongoClient
from lxml import etree
import urllib
import sys
import json
from phone import Phone
import pandas
newsary = []

headers = {'Cookie': 'ganji_xuuid=398ae62b-27dc-441c-bd98-84933f186948.1533604927143; ganji_uuid=3002735309777159034420; xxzl_deviceid=aSVUujZr2lvof9QQg%2B4KkCjyFr70Ux8KvFLU5DpPEwD4oqkHi8nyOA7Ppj1LDst9; cityDomain=zz; _wap__utmganji_wap_newCaInfo_V2=%7B%22ca_n%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_i%22%3A%22-%22%7D; lg=1; WantedListPageScreenType=1440; __utmc=32156897; __utmz=32156897.1533604953.1.1.utmcsr=zz.ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/; vip_version=new; pos_detail_zcm_popup=2018-8-7; xxzl_smartid=be401d0692a6d42f02d880b560949b8e; zcmDiversion=2018%2F8%2F7%3A2; gj_footprint=%5B%5B%22%5Cu53c9%5Cu8f66%5Cu5de5%5C%2F%5Cu94f2%5Cu8f66%5Cu5de5%22%2C%22%5C%2Fzpchachegong%5C%2F%22%5D%2C%5B%22%5Cu666e%5Cu5de5%5C%2F%5Cu5b66%5Cu5f92%5Cu5de5%22%2C%22%5C%2Fzpxuetugong%5C%2F%22%5D%2C%5B%22%5Cu755c%5Cu7267%5Cu5e08%22%2C%22%5C%2Fzpxmsxumushi%5C%2F%22%5D%5D; citydomain=zz; use_https=1; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A33727297404%2C%22kw%22%3A%22%E5%AD%A6%E5%8E%86%22%7D; __utma=32156897.1297944654.1533604953.1533604953.1533615642.2; GANJISESSID=1tbkfpcillfmenluedembp3so5; sscode=FQ2mTq376Nk93QgLFQBgVkQg; GanjiUserName=%23qq_705490237; GanjiUserInfo=%7B%22user_id%22%3A705490237%2C%22email%22%3A%22%22%2C%22username%22%3A%22%23qq_705490237%22%2C%22user_name%22%3A%22%23qq_705490237%22%2C%22nickname%22%3A%22%5Cu5f52%5Cu5c18%22%7D; bizs=%5B%5D; supercookie=AmN1AQxjZwZ3WTLlZzIyZmD5ZQD1LzWuMzD5MGH1LzZmAmAyZGL3AQMxZTV2MQR1AzR%3D; t3=2',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36',
            'Accept':'*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Referer':'https://www.ganji.com'
           }




keys = input("请输入关键字：")
# keys = "学历"
key = urllib.parse.quote(keys.encode("utf-8"))
num = -32
for i in range(70):
    num = num +32
    urls = "http://zz.ganji.com/site/s/f"+str(num)+"/_"+key+"/"
    print (urls)
    html = requests.get(urls).content
    dom = etree.HTML(html)
    _url = dom.xpath('//*[@id="js_list"]/div/dl/dt/a/@href')
    if not _url:
        break
    for i in _url:
        id = str(i).split("/")[2].strip('x|x.htm')
        # print id
        url = "http://www.ganji.com/pub/pub.php?act=pub&method=load&cid=11&jobinfo=241%2C2578&reply=103%3B"+str(id)+"%3B2&fbranch=i&domain=zz&is_iframe=1&from=viewFullPhone&source_position=wanted_detail_tel_pub"
        html2 = requests.get(url,headers=headers).content
        dom2 = etree.HTML(html2)
        try:
            name = dom2.xpath('//*[@id="simple_resume_base_field"]/div/div[2]/span[2]/text()')[0]
            phone = dom2.xpath('//*[@class="apply-pos-v2-tit"]/b/text()')[0]
        except Exception as e:
            print (e)

        # print(url , name , phone)
        phone_type = ''
        if len(phone) == 11:
            try:
                info = Phone().find(phone)
                phone_type = info["phone_type"]
            except:
                pass
        else:
            phone_type = "固话"
        print(name , phone , phone_type)
        newsary.append({'name': name , 'phone' : phone , 'phone_type' : phone_type })

newsary = set(newsary)
newsary = list(newsary)
newsdf = pandas.DataFrame(newsary)
newsdf.to_excel('ganji.xlsx')










