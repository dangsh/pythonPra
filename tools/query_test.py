from pyquery import PyQuery as pq
from lxml import etree

doc = pq(filename='page.html')
title = ''
cates = ''

with open('page.html',encoding='utf-8') as f:
selector = etree.HTML(html.text)
pic_Linklist = selector.xpath('//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')