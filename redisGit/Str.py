"""
redis提供两个类Redis和StrictRedis, 
StrictRedis用于实现大部分官方的命令，
Redis是StrictRedis的子类，用于向后兼用旧版本。
"""
# import redis
# # redis默认有16个数据库，db0-db15 ， 这里db=5是选择使用的数据库 
# # 向redis里插入数据后再读出来时所有键与值都是byte类型的，
# # decode_responses=True 将写入的键和值以str类型存储

# r = redis.Redis(host='localhost' , port='6379' , db=5 , decode_responses=True)
# r.set('name' , 'zhangsan')
# print(r.get('name'))   #输出 --> zhangsan

#默认redis存储的时候编码为 UTF-8 ，需要修改的话需要指定charset，例如
# r = redis.Redis(host='localhost' , port='6379' , db=5 , charset='GBK ' , decode_responses=True)

# redis使用connection pool来管理对一个redis server 的所有连接，
# 避免每次建立，释放连接的开销，
# 默认，每个Redis实例都会维护一个自己的连接池。
# 可以直接建立一个连接池，然后作为Redis的参数，
# 这样就可以实现多个Redis实例共享一个连接池。
# import redis

# pool = redis.ConnectionPool(host='localhost' , port='6379' , db=5 , decode_responses=True)
# r = redis.Redis(connection_pool = pool)
# r.set('name' , 'lisi')
# print(r.get('name'))   #输出 --> lisi


# import redis
# r = redis.Redis(host='localhost' , port='6379' , db=5 ,decode_responses=True)
# # r.lpush('xx' ,'zhangsan')
# # r.lpush('xx' ,'lisi')
# # r.lpush('xx' ,'wangwu')
# print(r.rpop('xx'))