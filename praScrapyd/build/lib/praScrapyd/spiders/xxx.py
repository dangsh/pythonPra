# -*- coding: utf-8 -*-
#   scrapyd-deploy --build-egg newnewnew.egg
import scrapy
from praScrapyd.items import PrascrapydItem

class XxxSpider(scrapy.Spider):
    name = 'xxx'
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
        # print(response.body.decode())
        for item in response.css(".cp-feedback"):
            cityName = item.css("::text").extract()
            print(cityName , "((((((((((((((((((((((((((((((((((((((((((((((((9")
            bb = PrascrapydItem()
            bb["cityName"] = cityName
            
            yield bb

        
        pass
