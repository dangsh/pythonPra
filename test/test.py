# def consumer():
#     status = True
#     while True:
#         n = yield status
#         print("我拿到了{}!".format(n))
#         if n == 3:
#             status = False
#
# def producer(consumer):
#     n = 5
#     while n > 0:
#         yield consumer.send(n)
#         n -= 1
#
# if __name__ == "__main__":
#     c = consumer() # 返回一个generator object
#     c.send(None) #将语句推进到第一个yield
#     p = producer(c) #定义了producer的生成器， 传入了consumer的生成器 ，让其进行通信
#     for status in p: #循环运行producer，获取它yield回来的状态
#         if status == False:
#             print("我只要3，4，5")
#             break
#     print("程序结束")

# import asyncio
#
# async def compute(x,y):
#     print("Compute %s + %s..." % (x,y))
#     await asyncio.sleep(1.0)
#     return x + y
#
# async def print_sum(x,y):
#     result = await compute(x,y)
#     print("%s + %s = %s" % (x,y,result))
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(print_sum(1,2))
# loop.close()

# import socket
#
# def sync_way():
#     for i in range(100):
#         sock = socket.socket()
#         sock.connect(('www.baidu.com' , 80))
#         print('connected')
#         request = 'GET {} HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(i))
#         sock.send(request.encode('ascii'))
#         response = b''
#         chunk = sock.recv(4096)
#         while chunk:
#             response += chunk
#             chunk = sock.recv(4096)
#         print('done!!')
#
# from time import time
# start = time()
# sync_way()
# end = time()
# print('Cost {} seconds'.format(end - start))


import socket
from selectors import DefaultSelector , EVENT_WRITE
selector = DefaultSelector()
sock = socket.socket()
sock.setblocking(False)
try:
    sock.connect(('www.baidu.com' , 80))
except BlockingIOError:
    pass

def connected():
    selector.unregister(sock.fileno())
    print('Connected!')
selector.register(sock.fileno() , EVENT_WRITE , connected())

