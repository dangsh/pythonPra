import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('a.html')

settings = {
    "template_path" : "templates" ,
    "static_path" : "statics" ,
}

application = tornado.web.Application([
    (r"/index" , MainHandler) ,
] , **settings)

if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()