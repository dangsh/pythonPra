import json
import redis
from pymongo import MongoClient


def read_data():
    try:
        for url in db.spark_company_url.find():
            r.lpush("com_url",url["_id"])
    except:
    	pass
    	
if __name__ == "__main__":
    conn = MongoClient('mongodb://192.168.14.90:27017/')
    db = conn.hy88
    r=redis.Redis(host='192.168.8.186',port='6379',db=1,decode_responses=True)
    read_data()