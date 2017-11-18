import scrapy


class MyfirstchongItem(scrapy.Item):
    title = scrapy.Field()
    targetUrl = scrapy.Field()    
    image_urls = scrapy.Field()
    # images = scrapy.Field()
    pass