from scrapy_redis.spiders import RedisSpider


class XxxSpider(RedisSpider):
    name = 'xxx'
    redis_key = "firstkey"


    def __init__(self , *args , **kwargs):
        domain = kwargs.pop("domain" , "")
        self.allow_domain = filter(None, domain.split(","))
        super(XxxSpider , self).__init__(*args , **kwargs)


    def parse(self, response):
        print("我是第一个爬虫 。。。。。。。。。。。。")
        pass
