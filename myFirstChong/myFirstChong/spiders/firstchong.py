#C:\Users\张霄港\Desktop\myFirstChong
import scrapy
from myFirstChong.items import MyfirstchongItem

class SpiderMan(scrapy.Spider):
    name="park"
    start_urls=[
        "https://doc.scrapy.org/en/latest/_static/selectors-sample1.html"
    ];
    def parse(self,response):
        for item in response.xpath("//div/a"):
            title=item.xpath("text()").extract()
            targetUrl=item.xpath("@href").extract()
            oneItem=MyfirstchongItem();
            oneItem["title"]=title
            oneItem["targetUrl"]=targetUrl;

            yield oneItem;