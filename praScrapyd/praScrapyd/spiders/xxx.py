# -*- coding: utf-8 -*-
import scrapy


class XxxSpider(scrapy.Spider):
    name = 'xxx'
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
        
        pass
