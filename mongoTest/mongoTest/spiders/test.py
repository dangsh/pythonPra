# -*- coding: utf-8 -*-
import scrapy
from pymongo import MongoClient
from mongoTest.items import MongotestItem
from scrapy import Request


class TestSpider(scrapy.Spider):
    name = 'test'
    
    start_urls = ['http://flights.ctrip.com/booking/XMN-BJS-day-1.html?DDate1=2016-04-19']
    db = MongoClient("127.0.0.1" , 27017)

    # print(db["mongo"])
    myDb = db["mongo"]
    students = myDb["worker"]
    # print(students)
    

    def parse(self, response):
        
        xiechengUrl = "http://flights.ctrip.com/booking/XMN-BJS-day-1.html?DDate1=2016-04-19"
        
        request = Request(xiechengUrl , headers=None , callback=self.parseResult)

        for item in response.css(".J_header_row"):
            print("(((((((((((((((((((((((")
            company = item.xpath("td[1]/div[1]/strong/text()").extract()
            planeType = item.xpath("td[1]/div[2]/span/text()").extract()
            airNumber = item.xpath("td[1]/div[1]/span/text()").extract()
            print(company , planeType , airNumber)
            # print(title)
            # TestSpider.students.insert({'name':title , 'age':13})



        
