from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class JavaScriptMiddleware(object):
    def process_request(self, request, spider):
        print("**************************************");
        if spider.name == "JD":

            driver = webdriver.Chrome("C:\\Users\张霄港\Desktop\chromedriver.exe") #指定使用的浏览器
            driver.get(request.url)
            time.sleep(1)
            js = "var q=document.documentElement.scrollTop=10000" 
            driver.execute_script(js) #可执行js，模仿用户操作。此处为将页面拉至最底端。       
            time.sleep(3)
            body = driver.page_source
            print ("访问"+request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return None
