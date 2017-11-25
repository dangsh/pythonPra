# -*- coding: utf-8 -*-
import scrapy


class XiechengSpider(scrapy.Spider):
    name = 'xiecheng'
    allowed_domains = ['http://flights.ctrip.com/booking/XMN-BJS-day-1.html?DDate1=2016-04-19']
    start_urls = ['http://flights.ctrip.com/booking/XMN-BJS-day-1.html?DDate1=2016-04-19']

    def parse(self, response):
        print("携程。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")
        pass
