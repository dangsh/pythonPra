#C:\Users\张霄港\Desktop\myFirstChong
import scrapy
from myFirstChong.items import MyfirstchongItem

class SpiderMan(scrapy.Spider):
    name="park";
    start_urls=[
        "http://v3.bootcss.com/css/"
    ];
    def parse(self,response):
        # response.selector.xpath("")===list;
        for item in response.xpath("//ul/li/a"):
            title=item.xpath("text()").extract()
            targetUrl=item.xpath("@href").extract()
            # print(item.xpath("a/@href").extract());
            oneItem=MyfirstchongItem();
            oneItem["title"]=title
            oneItem["targetUrl"]=targetUrl;
            oneItem["image_urls"]=["https://pic2.zhimg.com/v2-b4dc3fc47aa92ee9f3bd0571db9cffc9_r.png" , "http://ww3.sinaimg.cn/mw690/6941baebgw1erejj8h995j20sg08e75q.jpg"]
            # oneItem["images"]=

            yield oneItem;