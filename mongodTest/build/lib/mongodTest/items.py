# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MongodtestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    href = scrapy.Field();
    company = scrapy.Field();
    airType = scrapy.Field();
    startTime = scrapy.Field();
    startPlace = scrapy.Field();
    endTime = scrapy.Field();
    endPlace = scrapy.Field();
    BTS = scrapy.Field();
    favourable = scrapy.Field();
    destinationUrl = scrapy.Field();
    price = scrapy.Field();
    title = scrapy.Field();
    start = scrapy.Field();
    departure = scrapy.Field();
    thePrice = scrapy.Field();
    score = scrapy.Field();
    airNumber = scrapy.Field();
    pass
