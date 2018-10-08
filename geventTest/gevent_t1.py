# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()
import gevent
import time
from urllib  import urlopen



def say(url):
    response = urlopen(url)
    print len(response.read())

t1_start = time.time()
say('http://www.4399.com')
say('http://www.baidu.com')
say('http://www.sina.com')
print("normal---time cost",time.time() - t1_start)

t2_start = time.time()
gevent.joinall(
    [gevent.spawn(say,'http://www.4399.com'),
     gevent.spawn(say,'http://www.baidu.com'),
     gevent.spawn(say,'http://www.sina.com')]
)
print("gevent---time cost",time.time() - t2_start)