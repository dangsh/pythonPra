# -*- coding: utf-8 -*-
import scrapy


class Baidu1Spider(scrapy.Spider):
    name = 'baidu1'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print("我是百度蜘蛛")
        pass
