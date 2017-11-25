import scrapy
from scrapy.spider import Spider
import selenium

class JingDongSpider(Spider):
    name = "JD"
    start_urls = [
        "http://wap.jd.com/category/all.html"
    ]

    def parse(self , response):
        for item in response.css(".mc"):
            title = item.css(".p-name a::text").extract()
            print(title)
            