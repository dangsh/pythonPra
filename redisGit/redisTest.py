#-----------1-lrange-------------
# import redis
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.lpush("0",1,2,3,4) 
# print(r.lrange("0" , 0 , -1))
# print(r.lrange("0" , 0 , 0))
#-----------2-lpush-------------
# import redis
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.lpush("1",1) 
# print(r.lrange("1" , 0 , -1)) #打印列表"1"的全部内容
# r.lpush("1",1,2,3,4)
# print(r.lrange("1" , 0 , -1))

#-----------3-rpush-------------
# import redis
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("2",1) 
# print(r.lrange("2" , 0 , -1)) #打印列表"1"的全部内容
# r.rpush("2",1,2,3,4)
# print(r.lrange("2" , 0 , -1))

#-----------4-lpop-------------
# import redis
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.lpush("3",1,2,3,4)
# print(r.lrange("3" , 0 , -1)) #打印列表"3"的全部内容
# r.lpop("3")
# print(r.lrange("3" , 0 , -1))

#-----------5-rpop-------------
# import redis
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.lpush("4",1,2,3,4)
# print(r.lrange("4" , 0 , -1)) #打印列表"4"的全部内容
# r.rpop("4")
# print(r.lrange("4" , 0 , -1))

#-----------6-blpop-------------
# import redis 
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("6",1,2,3,4,4,5,6)
# print(r.blpop("6"))
# print(r.blpop("6"))
# print(r.blpop("6"))
# print(r.blpop("100" , timeout=2))
# print(r.lrange("6" , 0 , -1)) #打印列表"6"的全部内容
#-----------7-brpop-------------
# import redis 
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("7",1,2,3,4,5,6,)     
# print(r.lrange("7" , 0 , -1)) #打印列表"7"的全部内容 
# print(r.brpop("7"))     
# print(r.brpop("7"))     
# print(r.brpop("7"))      
# print(r.brpop("101",timeout=2))      #因为键 101 不存在，所以2秒后输出的结果是None
# print(r.lrange("7" , 0 , -1)) #打印列表"7"的全部内容 
#-----------8-brpoplpush-------------
# import redis 
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("8",1,2,3)
# r.rpush("88",4,5,6)
# print(r.lrange("8" , 0 , -1)) #打印列表"8"的全部内容 
# print(r.lrange("88" , 0 , -1)) #打印列表"88"的全部内容 
# print(r.brpoplpush(src="8",dst="88",timeout=2))  #输出的结果是3
# print(r.brpoplpush(src="44",dst="22",timeout=2))  #键44 不存在，输出的结果是None
# print(r.lrange("8" , 0 , -1)) #打印列表"8"的全部内容 
# print(r.lrange("88" , 0 , -1)) #打印列表"88"的全部内容 
#-----------9-lindex-------------
# import redis 
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("9",1,2,3)
# print(r.lrange("9" , 0 , -1)) #打印列表"8"的全部内容 
# print(r.lindex("9",0))        #输出的结果是1
# print(r.lindex("9",1))        #输出的结果是2
# print(r.lindex("9",2))        #输出的结果是3
# print(r.lindex("9",3))        #输出的结果是None
# print(r.lindex("9",-1))        #输出的结果是3
# print(r.lrange("9" , 0 , -1)) #打印列表"8"的全部内容 
#-----------10-linsert-------------
# import redis 
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("10",1,2,3)
# print(r.lrange("10" , 0 , -1)) #打印列表"10"的全部内容 
# r.linsert("10" , "BEFORE" , "2" , 10)
# print(r.lrange("10" , 0 , -1)) #结果 ['1', '10', '2', '3']

# r.rpush("100",1,2,3)
# r.linsert("100" , "AFTER" , "2" , 10)
# print(r.lrange("100" , 0 , -1)) #结果 ['1', '2', '10', '3']
#-----------11-llen-------------
# import redis 
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("11",1,2,3)
# print(r.lrange("11" , 0 , -1)) #打印列表"11"的全部内容 
# print(r.llen("11"))
#-----------12-lpushx-------------
# import redis 
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("12" , 1,2,3)
# r.rpush("122" , 1,2,3)
# print(r.lrange("12" , 0 , -1)) #结果为 ['1', '2', '3']
# print(r.lrange("122" , 0 , -1)) #结果为 ['1', '2', '3']
# r.lpush("123" , 1)
# r.lpushx("1223" , 1)
# print(r.lrange("123" , 0 , -1)) #结果为 ['1']
# print(r.lrange("1223" , 0 , -1)) #结果为 []
#-----------13-lrem-------------
# import redis 
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("13" , 'a','b','b','c','d','b')
# print(r.lrange("13" , 0 , -1)) #['a', 'b', 'b', 'c', 'd', 'b']
# r.lrem("13" , "b" , 2)
# print(r.lrange("13" , 0 , -1)) #['a', 'c', 'd', 'b']

# r.rpush("133" , 'a','b','b','c','d','b')
# print(r.lrange("133" , 0 , -1)) #['a', 'b', 'b', 'c', 'd', 'b'] 
# r.lrem("133" , "b" , -2)
# print(r.lrange("133" , 0 , -1)) #['a', 'b', 'c', 'd']

#-----------14-lset-------------
# import redis
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("14" , 1,2,3,4)
# print(r.lrange("14" , 0 , -1)) #打印列表"14"的全部内容
# r.lset("14",1,9)
# print(r.lrange("14" , 0 , -1)) #结果为 ['1', '9', '3', '4']

#-----------15-ltrim-------------
# import redis
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("15" , 1,2,3,4)
# print(r.lrange("15" , 0 , -1)) #打印列表"14"的全部内容
# r.ltrim("15",0,1)
# print(r.lrange("15" , 0 , -1)) #结果为 ['1', '2']
#-----------16-rpoplpush-------------
# import redis 
# r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# r.rpush("16",1,2,3)
# r.rpush("166",4,5,6)
# print(r.lrange("16" , 0 , -1)) # ['1', '2', '3'] 
# print(r.lrange("166" , 0 , -1)) # ['4', '5', '6'] 
# print(r.rpoplpush(src="16",dst="166"))  #输出的结果是3
# print(r.lrange("16" , 0 , -1)) # ['1', '2'] 
# print(r.lrange("166" , 0 , -1)) # ['3', '4', '5', '6']
#-----------17-rpushx-------------
import redis 
r = redis.Redis(host='localhost' , port='6379' , db=6 ,decode_responses=True)
# for i in range(10):
#     r.lpop("17")
#     r.lpop("177")
#     r.lpop("1777")
r.rpush("17" , 1,2,3)
r.rpush("177" , 1,2,3)
print(r.lrange("17" , 0 , -1)) #结果为 ['1', '2', '3']
print(r.lrange("177" , 0 , -1)) #结果为 ['1', '2', '3']
r.rpush("177" , 4)
r.rpushx("1777" , 4)
print(r.lrange("177" , 0 , -1)) #结果为 ['1', '2', '3', '4']
print(r.lrange("1777" , 0 , -1)) #结果为 []