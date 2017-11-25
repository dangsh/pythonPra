# -*- coding: utf-8 -*-
import scrapy


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['wap.jd.com/category/all.html']
    start_urls = ['http://wap.jd.com/category/all.html/']

    def parse(self, response):
        pass
