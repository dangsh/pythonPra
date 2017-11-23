import scrapy
from scrapy.spider import Spider
import selenium

class JingDongSpider(Spider):
    name = "JD"
    start_urls = [
        "http://wap.jd.com/category/all.html"
    ]

    def parse(self , response):
        for item in response.css(".fore1"):
            title = item.xpath("a/text()").extract()
            print(title)
            