# -*- coding: utf-8 -*-
import scrapy


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['www.sina.com']
    start_urls = ['http://www.sina.com/']

    def parse(self, response):
        print("我是新浪蜘蛛")
        pass
