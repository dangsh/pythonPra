# -*- coding: utf-8 -*-
import scrapy


class KeeperSpider(scrapy.Spider):
    name = 'keeper'
    start_urls = ['https://www.douban.com/doulist/36980/']

    print("aaaaaaaaa")
    def parse(self, response):
        for item in response.css(".doulist-subject .title"):

            print("(((((((((((((((((((((((")
            movieName = item.xpath("a/text()").extract()
            

            it = MongotestItem()
            it["movieName"] = movieName
            yield movieName 
