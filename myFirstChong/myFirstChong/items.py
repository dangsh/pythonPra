import scrapy


class MyfirstchongItem(scrapy.Item):
    title = scrapy.Field()
    targetUrl = scrapy.Field()    
    pass