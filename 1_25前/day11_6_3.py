# rank-view-list li
import requests
from bs4 import BeautifulSoup
import pandas

newsary = []



res=requests.get('http://r.qidian.com/yuepiao?chn=-1&page=1')
soup = BeautifulSoup(res.text , 'html.parser') 
# print(soup)
for news in soup.select('.rank-view-list li'): #定位
    print(news.select('a')[1].text,news.select('a')[2].text,news.select('a')[3].text,news.select('p')[1].text,news.select('p')[2].text,news.select('a')[0]['href'])
    # print(news)
    