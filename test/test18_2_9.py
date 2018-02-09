# class Student(object):
#     def __init__(self , name , score):
#         self.__name = name
#         self.__score = score
#     def print_score(self):
#         print('%s:%s'%(self.__name ,  self.__score))
#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
#     def set_name(self , name):
#         self.__name = name
#     def set_score(self , score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('error score')
#
#     def get_grade(self):
#         if self.score >=90:
#             return 'a'
#         elif self.score >=60:
#             return 'b'
#         else:
#             return 'c'
#
# b = Student('bbb',1)
# print(b.get_score())
# b.set_score(1111)
# print(b.get_score())

# class Animal(object):
#     def run(self):
#         print('Animal is running')
# class Dog(Animal):
#     def run(self):
#         print('Dog is runnig..')
#     def eat(self):
#         print('Eating meat..')
#
# class Cat(Animal):
#     def run(self):
#         print('Cat is running ...')
#
# # dog = Dog()
# # dog.run()
# # dog.eat()
# class Timer(object):
#     def run(self):
#         print('hhhhhhhhhhhhhhhhhhhhhhhhh')
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# run_twice(Timer())

# class Student(object):
#     @property
#     def get_score(self):
#         return self._score
#     @score.setter
#     def set_score(self , value):
#         if not isinstance(value , int):
#             raise ValueError('score must be an integer')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100')
#         self._score = value
#
# s = Student()
# s.set_score(60)
# print(s.get_score())
#
# s.set_score(9999)

# class Student(object):
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self , value):
#         if not isinstance(value , int):
#             raise ValueError('score must be an intefger')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100')
#         self._score = value
# s = Student()
# s.score = 60 #转化为s.set_score(60)
# print(s.score) #转化为s.get_score()
# s.score = 999

# class Student(object):
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self , value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2017 - self._birth
# s = Student()
# s.birth = 1990
# print(s.birth)
# print(s.age)
# s.age = 50
# print(s.age)


# class Animal(object):
#     pass
#
# #大类
# class Mammal(Animal):
#     pass
# class Bird(Animal):
#     pass
#
# class Runnable(object):
#     def run(self):
#         print('Running .............')
#
# class Flyable(object):
#     def flr(self):
#         print('Flying')
#
# #各种动物
# class Dog(Mammal , Runnable):
#     pass
# class Bat(Mammal , Flyable):
#     pass
# class Parrot(Bird):
#     pass
# class Ostrich(Bird):
#     pass
#
#
#
# d = Dog()
# d.run()

# class Student(object):
#     def __init__(self , name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name:{})'.format(self.name)
#
# # print(Student('Michael'))

# class Fib(object):
#     def __init__(self):
#         self.a , self.b = 0 , 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a , self.b = self.b , self.a + self.b
#         if self.a > 1000:
#             raise StopIteration()
#         return self.a
# for n in Fib():
#     print(n)
# # Fib()[5]

# class Fib(object):
#     def __getitem__(self, n):
#         a , b = 1 , 1
#         for x in range (n):
#             a , b = b , a + b
#         return a
# f = Fib()
# for i in range(10):
#     print(f[i])

# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'
#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 99
#
# s = Student()
# print(s.name)
# print(s.score)

# class Student(object):
#     def __init__ (self , name):
#         self.name = name
#     def __call__(self):
#         print('My name is %s' % self.name)
# s = Student('ABB')
# s()

# from enum import Enum
# Month = Enum('Month',('Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun'))
# for name , member in Month.__members__.items():
#     print(name,'=>',member,',',member.value)

# class Hello(object):
#     def hello(self , name='workd'):
#         print('Hello , %s' % name)

# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10/n
# def main():
#     foo('0')
# main()

# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10/n)

# try:
#     f = open('d:/pythonPra/test/test.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open('d:/pythonPra/test/test.txt' , 'r') as f:
#     for line in f.readlines():
#         print(line.strip())
#     # print(f.read())

# f = open('d:/pythonPra/test/6.jpg' , 'rb')
# print(f.read())

# f = open('d:/pythonPra/test/test.txt' , 'r' , encoding='utf-8' , errors='ignore')
# print(f.read())

# f = open('d:/pythonPra/test/test.txt' , 'a')
# f.write('\n Hello World')
# f.close()

# loop = get_event_loop()
# while True:
#     event = loop.get_event()
#     process_event(event)

# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s ...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PEODUCER] Consumer return : %s' % r)
#     c.close()
#
# c = consumer() # consumer 是一个生成器
# produce(c) # 把生成器传入produce
# """
# 1.调用c.send(None)
# 2.产生东西之后通过c.send(n) 切换到consumer执行
# 3.consumer 通过 yield 拿到消息，处理，又通过yield把消息传回
# 4.produce拿到consumer处理的结果，继续生产下一条消息
# 5.produce 不生产了，通过c.close() 关闭consumer，整个过程结束
# 整流程无锁，由一个线程执行，produce和consumer协助完成任务，所以称为“协程”
# """

# import threading
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello World (%s)" % threading.currentThread())
#     #异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello Again (%s)" % threading.currentThread())
# #获取EventLoop
# loop = asyncio.get_event_loop()
# tasks = [hello() , hello()]
# #执行coroutine
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# import asyncio
# @asyncio.coroutine
# def wget(host):
#     print('wget %s ...' % host)
#     connect = asyncio.open_connection(host , 80)
#     reader , writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host , line.decode('utf-8').rstrip()))
#     writer.close()
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn' , 'www.sohu.com' , 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
# import threading
# import asyncio
#
# async def hello():
#     print("hello world (%s)" % threading.currentThread())
#     r = await asyncio.sleep(1)
#     print("Hello again! (%s)" % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello() , hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


