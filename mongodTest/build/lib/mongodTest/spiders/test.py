import scrapy
from scrapy.spiders import Spider
import time
from mongodTest.items import MongodtestItem

class Qunar(scrapy.Spider):
    name = 'qunar';
    start_urls = [
        "http://www.qunar.com"
    ]
    def parse(self, response):
        for item in response.xpath("//ul[@class = 'clrfix']/li/a"):
            title = item.xpath("@title").extract();
            # destinationUrl = item.xpath("@href").extract();
            oneItem = MongodtestItem();
            oneItem['title'] = title;
            yield oneItem;