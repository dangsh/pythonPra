import happybase
import random

conn = happybase.Connection('192.168.14.1', 9090)
table = conn.table("201619240214")
for i in range(1000):
    table.put(str(i+1), {"liutaicheng:1": random.randint(1,10000),"liutaicheng:2": random.randint(1,10000),"liutaicheng:3": random.randint(1,10000),"liutaicheng:4": random.randint(1,10000),"liutaicheng:5": random.randint(1,10000),"liutaicheng:6": random.randint(1,10000),"liutaicheng:7": random.randint(1,10000),"liutaicheng:8": random.randint(1,10000),"liutaicheng:9": random.randint(1,10000),"liutaicheng:10": random.randint(1,10000),})




