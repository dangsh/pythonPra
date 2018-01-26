import tornado.ioloop
import tornado.web
from tornado import httpclient
from tornado.web import asynchronous
from tornado import gen
import uimodules as md
import uimethods as mt

class MainHandler(tornado.web.RedirectHandler):
    @asynchronous
    @gen.coroutine
    def get(self):
        print('start get')
        http = httpclient.AsyncHTTPClient()
        http.fetch("http://127.0.0.1:8008/post/" , self.callback)
        self.write('end')
    def callback(self , response):
        print(response.body)



application = tornado.web.Application([
    (r'/index' , MainHandler),
])

if __name__ == "__main__":
    application.listen(8009)
    tornado.ioloop.IOLoop.instance().start()