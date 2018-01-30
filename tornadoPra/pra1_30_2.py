import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('2.html')

class CMDBHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('CMDB')

settings = {
    "template_path" : "templates" ,
    "static_path" : "statics" ,
    "static_url_prefix" : "/static/" ,
}
application = tornado.web.Application([
    (r"/index" , MainHandler) ,
    (r"/cmdb" , CMDBHandler)
] , **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()