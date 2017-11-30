from scrapy_redis.spiders import RedisSpider


class YyySpider(RedisSpider):
    name = 'yyy'
    
    redis_key = "secondkey"

    def __init__(self , *args , **kwargs):
        domain = kwargs.pop("domain" , "")
        self.allow_domain = filter(None, domain.split(","))
        super(YyySpider , self).__init__(*args , **kwargs)


    def parse(self, response):
        print("我是第二个爬虫 XXXXXXXXXXXXXXXXXXXx")
        pass
