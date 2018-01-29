import os
import tornado.web
import tornado.ioloop

class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello , ADD\n")
    
class DeleteHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello , DELETE\n")

class UpdateHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello , UPDATE\n")

class SelectHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello , SELECT\n")


if __name__ == "__main__":
    settings = {
        'debug' : True,
        'static_path' : os.path.join(os.path.dirname(__file__) , "static") ,
        'template_path' : os.path.join(os.path.dirname(__file__) , "template") ,
    }

    application = tornado.web.Application([
        (r"/add" , AddHandler),
        (r"/delete" , DeleteHandler),
        (r"/update" , UpdateHandler),
        (r"/select" , SelectHandler),

    ] , **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


