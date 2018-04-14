# import json
# from pymongo import MongoClient
# def read_data():
#     with open('big2.json' , encoding='utf-8') as f:
#         for i in range(3910239):
#             line = f.readline()
#             d = json.loads(line)
#             url = d["url"]
#             make_insert(url)
#             # if select(goodsid) == 0:
#             # 	make_insert(goodsid)
#             # else:
#             # 	pass
#     f.close()

# def make_insert(url):
#     try:
#         db.huangye88_product_url.insert({'_id':url})
#     except:
#         pass



# if __name__ == "__main__":
#     conn = MongoClient('mongodb://192.168.14.90:27017/')
#     db = conn.zkp
#     read_data()

import json
from pymongo import MongoClient
def read_data():
    with open('big2.json' , encoding='utf-8') as f:
        for i in range(3910239):
            line = f.readline()
            d = json.loads(line)
            url = d["url"]
            make_insert(url)
            # if select(goodsid) == 0:
            #   make_insert(goodsid)
            # else:
            #   pass
    f.close()

def make_insert(url):
    try:
        db.huangye88_product_url.insert({'_id':url})
    except:
        pass



if __name__ == "__main__":
    conn = MongoClient('mongodb://192.168.14.90:27017/')
    db = conn.zkp
    read_data()
#     