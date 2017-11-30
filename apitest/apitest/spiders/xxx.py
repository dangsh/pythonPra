# -*- coding: utf-8 -*-
import scrapy


class XxxSpider(scrapy.Spider):
    name = 'xxx'
    allowed_domains = ['www.4399.com']
    start_urls = ['http://www.4399.com/']

    def parse(self, response):
        pass
