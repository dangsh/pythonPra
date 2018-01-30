import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self , user , pwd):
        self.write("Hello ,%s is %s"%(user,pwd))

class CMDBHandler(tornado.web.RequestHandler):
    def get(self , num):
        self.write('CMDB id %s' % num)

settings = {
    "template_path" : "templates" ,
    "static_path" : "statics" ,
    "static_url_prefix" : "/static/" ,
}
application = tornado.web.Application([
    (r"/index/(?P<user>.*)/(?P<pwd>.*)" , MainHandler) ,
    (r"/cmdb/(\w+)" , CMDBHandler) ,
] , **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

