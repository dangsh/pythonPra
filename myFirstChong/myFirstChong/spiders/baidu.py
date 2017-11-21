# https://passport.baidu.com/v2/api/?login
# https://passport.baidu.com/v2/getpublickey?token=4647fb8d22b56a0c36dba2e9b5e31460&tpl=mn&apiver=v3&tt=1511179299539&gid=36EB853-5B2C-45E8-8716-5A2BD07C090B&traceid=&callback=bd__cbs__vuhaqz
# https://sp1.baidu.com/8qUJcD3n0sgCo2Kml5_Y_D3/v.gif?pid=201&pj=www&fm=behs&tab=tj_login&query=&un=&path=https%3A%2F%2Fwww.baidu.com%2F&wd=&rsv_sid=1469_21103&rsv_did=73a4985f823f21536108fada5ce68ff9&t=1511179673003
import scrapy
from scrapy.spiders import Spider
from scrapy.http import Request
import time
import re

myHead = {
    "Content-Type":"application/x-www-form-urlencoded",
    "Origin":"https://www.baidu.com",
    "Upgrade-Insecure-Requests":1,
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Connection":"keep-alive" ,
    "Accept-Language" : "zh-CN,zh,1=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Cache-Control":"no-cache" ,
    "Pragma":"no-cache",
    "Host":"www.baidu.com"


}

myHead = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Host":"passport.baidu.com",
    "Pragma":"no-cache",
    "Upgrade-Insecure-Requests":1,
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
 
}

class BaiduScrapy(Spider):
    name = "baidu"
    start_urls = [
        "https://www.baidu.com"
    ]

    def parse(self , response):
        #获取百度首页
       
        request = Request("https://www.baidu.com" , headers = myHead , callback = self.parseHomeFn)
        return request
    
    def parseHomeFn(self , response):
        print("开始解析百度首页")
        if response.status == 200:
            print("开始请求token。。。。。。。。。。。。")
            yield self.getTokenFn()

        else:
            print("请求百度首页出错")
        



    def getFnName(self):
        fnName = "bd__cbs__%d" % time.time()
        print("回调函数name:--------------%s" % fnName)  
        return fnName

    def getGid(self):
        return "54DEF72-683A-4D40-B973-69EE29C92681"

    #token 方法
    def getTokenFn(self):
        baiduTokenUrl = "https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=login&logintype=basicLogin&tt="+"%d"%(time.time() * 1000) + "&callback=" + self.getFnName() + "&gid=" + self.getGid() 
        request = Request(baiduTokenUrl , headers=myHead , callback = self.parseTokenFn)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return request 

        
        # myHead["Host"] = "passport.baidu.com"
        # aaa = "https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=login&logintype=basicLogin"+"&tt="+'%d' % (time.time() * 1000)+"&callback="+self.getFnName()+"&gid="+self.getGid()
        # request = Request(aaa, headers=myHead, callback=self.parseTokenFn)
        # return request
    #解析token的方法
    def parseTokenFn(self , response):
        print("正在解析token值。。。。。。。。。。。。。。。")
        if response.status == 200:
            print("获取token数据成功")

            guize = re.compile('\"token\"\s+:\s+"(\w+)\"')
            myData = guize.findall(response.body.decode())[0]
            print(myData)
        else:
            print("获取token数据失败")

    #获取验证码 和 输入验证
