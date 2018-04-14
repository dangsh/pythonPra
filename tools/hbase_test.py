import happybase
conn = happybase.Connection('192.168.14.1',9090)
table = conn.table("spider_hc360")
def write_data_to_db(url , response , data):
    table.put(url , {"info:content":response , "info:data":data})

if __name__ == "__main__":
    write_data_to_db("1","2","3")

    