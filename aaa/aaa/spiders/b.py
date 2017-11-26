# -*- coding: utf-8 -*-
import scrapy


class BSpider(scrapy.Spider):
    name = 'b'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
