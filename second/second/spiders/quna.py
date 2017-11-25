# -*- coding: utf-8 -*-
import scrapy


class QunaSpider(scrapy.Spider):
    name = 'quna'
    allowed_domains = ['https://www.qunar.com/']
    start_urls = ['https://www.qunar.com//']

    def parse(self, response):
        print("去哪。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")
        pass
