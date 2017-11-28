from scrapy.conf import settings
from pymongo import MongoClient

# MONGO_HOST
# MONGO_PORT
# MONGO_DBNAME
# MONGO_COLLECTION


class MongopipClass():
    
    def __init__(self):
        print("%%%%%%%%%%%%%%%%%%%%%%%%");
        client = MongoClient(settings["MONGO_HOST"] , settings["MONGO_PORT"]);
        myDB = client[settings["MONGO_DBNAME"]];
        self.myCollection = myDB[settings["MONGO_COLLECTION"]];
        # print(col);
       
    
    def process_item(self , item , spider):
        print("&&&&&&&&&&&&&&");
        self.myCollection.insert({"name":item["title"]});
        
        return item;
    