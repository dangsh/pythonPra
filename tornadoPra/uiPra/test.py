import tornado.web
import tornado.ioloop
import uimethod
import uimodule
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("tem.html" , name = "Lili")

settings = {
    "ui_methods" : uimethod ,
    "ui_modules" : uimodule
}

application = tornado.web.Application([
    (r'/' , MainHandler),
] , **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()