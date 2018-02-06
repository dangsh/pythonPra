from multiprocessing import Process
import os

#多进程
# def run_proc(name):
#     print('Run chiled process %s (%s)...' % (name , os.getpid()))
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target = run_proc , args = ('test' ,))
#     p.start()
#     p.join()
#     print('End')

#多线程
# import time , threading
# def loop():
#     print('Thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print("thread %s >>> %d" % (thread_name , n))
#     print('Thread %s ends.' % thread_name)
#
# thread_name = threading.current_thread().name
# print('Thread %s is running...' % thread_name)
# t = threading.Thread(target = loop , name = 'loopThread')
# t.start()
# t.join()
# print('Thread %s ends.' % thread_name)

#多线程银行问题
# import threading
# import time
#
# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# # def run_thread(n):
# #     for i in range(10):
# #         change_it(n)
#
# #加锁 保证安全
# def run_thread(n):
#     for i in range(10000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
#
# t1 = threading.Thread(target=run_thread , args=(5 ,))
# t2 = threading.Thread(target=run_thread , args=(5 ,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# 线程安全的队列 保证了多线程下是安全的
# import queue
# import threading
#
# q = queue.Queue()
# for i in range(5):
#     q.put(i)
# while not q.empty():
#     print(q.get())
# print("------------------")
# q = queue.LifoQueue()
# for i in range(5):
#     q.put(i)
# while not q.empty():
#     print(q.get())
# print("------------------")
#
# class Task:
#     def __init__ (self , priority , description):
#         self.priority = priority
#         self.description = description
#
#     def __lt__(self , other):
#         return self.priority < other.priority
#
# q = queue.PriorityQueue()
# q.put(Task(1 , 'Important task'))
# q.put(Task(10 , 'Normal task'))
# q.put(Task(100 , 'Lazy task'))
#
# def job(q):
#     while True:
#         task = q.get()
#         print('Task:' , task.description)
#         q.task_done()
#
# threads = [threading.Thread(target=job , args=(q , )),
#            threading.Thread(target=job, args=(q,))
#            ]
# for t in threads:
#     t.setDaemon(True)
#     t.start()
# q.join()

#测试cpu压力
# import multiprocessing
# import threading
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

# import threading
# local_school = threading.local()
# def process_student():
#     std = local_school.student
#     print('Hello %s (%s)' % (std , threading.current_thread().name))
#
# def process_thread(name):
#     local_school.student = name
#     process_student()
#
# t1 = threading.Thread(target=process_thread , args=('Tom' ,) , name='TA')
# t2 = threading.Thread(target=process_thread , args=('JACK' ,) , name='TB')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#-------------------------------------

