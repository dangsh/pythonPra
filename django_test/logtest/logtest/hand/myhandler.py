#coding:utf-8
import logging
import redis

class Testtt(logging.StreamHandler):
    def emit(self, record):
        msg = self.format(record)
        print "11111111111111",msg
        r = redis.Redis(host='192.168.8.186', port='6379', db=2, decode_responses=True)
        r.lpush("sql", msg)
