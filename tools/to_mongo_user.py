import json
from pymongo import MongoClient
def read_data():
    with open('test14.json' , encoding='utf-8') as f:
        for i in range(202509):
            line = f.readline()
            d = json.loads(line)
            userid = d["userid"]
            make_insert(userid)
    f.close()

def make_insert(userid):
    db.userid.insert({'userid':userid})

if __name__ == "__main__":
    conn = MongoClient('mongodb://192.168.14.90:27017/')
    db = conn.ali
    read_data()

