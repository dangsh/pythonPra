import json
import redis
from pymongo import MongoClient
# def read_data():
# 	with open('goods_url.json',encoding='utf-8') as f:
# 		for i in range(54263949):
# 		# for i in range(10):
# 			line=f.readline()
# 			a = line[:-2]
# 			d = json.loads(a)
# 			url = d["goods_url"][0]
# 			new_url = 'https:' + url
# 			r.lpush("hcSpider:start_urls",new_url)

def read_data():
    for url in db.spark_test.find():
    	# print(url["_id"])
        r.lpush("url",url["_id"])

if __name__ == "__main__":
    conn = MongoClient('mongodb://192.168.14.90:27017/')
    db = conn.test
    r=redis.Redis(host='192.168.8.186',port='6379',db=0,decode_responses=True)
    read_data()