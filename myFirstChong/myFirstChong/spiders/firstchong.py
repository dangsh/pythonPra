#C:\Users\张霄港\Desktop\myFirstChong
import scrapy
from myFirstChong.items import MyfirstchongItem

class SpiderMan(scrapy.Spider):
    name = "park"
    start_urls = [
        "http://v3.bootcss.com/css/"
    ]

    def parse(self , response):
        for item in response.xpath("//ul/li/a"):
            # print(item.xpath("@href").extract())
            title = item.xpath("text()").extract()
            targetUrl = item.xpath("@href").extract()

            oneItem = MyfirstchongItem()
            oneItem["title"] = title
            oneItem["targetUrl"] = targetUrl
            # print(oneItem)
            yield oneItem
