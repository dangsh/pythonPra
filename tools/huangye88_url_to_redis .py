import json
import redis
from pymongo import MongoClient


def read_data():
    for url in db.quchong_url.find():
        r.lpush("url",url["_id"])

if __name__ == "__main__":
    conn = MongoClient('mongodb://192.168.14.90:27017/')
    db = conn.hy88
    r=redis.Redis(host='192.168.8.186',port='6379',db=0,decode_responses=True)
    read_data()