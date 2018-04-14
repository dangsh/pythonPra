import json
from pymongo import MongoClient
def read_data():
    with open('shopData1.json' , encoding='utf-8') as f:
        for i in range(3227):
            line = f.readline()
            d = json.loads(line)
            shopid = d["shopid"]
            make_insert(shopid)
    f.close()

def make_insert(shopid):
    db.shopid.insert({'shopid':shopid})

if __name__ == "__main__":
    conn = MongoClient('mongodb://192.168.14.90:27017/')
    db = conn.ali
    read_data()

