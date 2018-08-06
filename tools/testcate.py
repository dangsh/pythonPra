#https://detail.1688.com/offer/574931737002.html
from pymongo import MongoClient
import requests
import re
for i in range(1000):
	num = 574931737002
	url = 'https://detail.1688.com/offer/' + str(num+i) + '.html'
	response = requests.get(url)
	response = response.text
	reg = "'catid':'(.*?)',"
	result = re.findall(reg,response)
	if result:
		result = result[0]
	else:
		print(url , '$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		continue
	print(result)
	client = MongoClient("192.168.14.90" , 27017)
	myDb = client["ali"]
	myCollection = myDb["cate"]
	a = myCollection.find_one({'_id':int(result)})
	print(a)
	if not a:
		print(url , result , '@@@@@@@@@@@@@@@@@@@@@@@@')