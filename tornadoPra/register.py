import tornado.ioloop
import tornado.web
import  xo
import  ox
class MainHandler(tornado.web.RequestHandler):
    def get(self , user , pwd):
        self.write("Hello,%s,is %s"%(user , pwd))
class CMDBHandler(tornado.web.RequestHandler):
    def get(self , num):
        self.write("CMDB is %s"%num)
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("regis.html")
settings = {
    "template_path" : "template" ,
    "static_path" : "statics" ,
    "ui_methods" : xo ,
    "ui_modules" : ox ,
}
appliction = tornado.web.Application([
    (r"/index/(?P<user>.*)/(?P<pwd>.*)" , MainHandler) ,
    (r"/cmdb/(\w+)" , CMDBHandler) ,
    (r"/test" , TestHandler) ,
])
if __name__ == "__main__":
    appliction.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
