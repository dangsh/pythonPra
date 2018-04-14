import requests
from lxml import etree
from pymongo import MongoClient

def read_data():
	response = requests.get('https://index.hc360.com/inMarket/?scode=020006001')
	selector = etree.HTML(response.text)
	for i in selector.xpath('//div[@id="3len"]/div[@class="selectCon"]/ul/li/a'):
		catename = i.xpath('text()')
		url = i.xpath('@href')
		full_url = 'https://index.hc360.com' + url[0]
		try:
			db.huicong_level.insert({'catename':catename[0] , 'url':full_url , 'level':1})
		except:
			pass

# db.getCollection('huicong_level').find({"_id" : ObjectId("5ab8c0bcd59a2e04c8f03d79")})
def read_data2():
	data = select()
	for i in data:
		url = i['url']
		id = i['_id']
		response = requests.get(url)
		selector = etree.HTML(response.text)
		for i in selector.xpath('//div[@id="6len"]/div[@class="selectCon"]/ul/li/a'):
			catename = i.xpath('text()')
			url = i.xpath('@href')
			full_url = 'https://index.hc360.com' + url[0]
			try:
				db.huicong_level.insert({'catename':catename[0] , 'url':full_url , 'cate1_id':id , 'level':2})
			except:
				pass


def read_data3():
	data = select_level2()
	for i in data:
		url = i['url']
		cate1_id = i['cate1_id']
		cate2_id = i['_id']
		response = requests.get(url)
		selector = etree.HTML(response.text)
		try:
			for i in selector.xpath('//div[@id="9len"]/div[@class="selectCon"]/ul/li/a'):
				catename = i.xpath('text()')
				url = i.xpath('@href')
				full_url = 'https://index.hc360.com' + url[0]
				try:
					db.huicong_level.insert({'catename':catename[0] , 'url':full_url , 'cate1_id':cate1_id , 'cate2_id':cate2_id ,'level':3})
				except:
					pass
		except:
			print(url + '没有第三级目录')


def select():
	return db.huicong_level.find({})

def select_level2():
	return db.huicong_level.find({'level':2})

if __name__ == "__main__":
	conn = MongoClient('mongodb://192.168.14.90:27017/')
	db = conn.ali
	read_data3()
