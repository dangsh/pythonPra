import os
import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello , SELECT\n")
    
    def post(self):
        self.write("hello , ADD\n")
    
    def put(self):
        self.write("hello , UPDATE\n")

    def delete(self):
        self.write("hello , DELETE\n")


if __name__ == "__main__":
    settings = {
        'debug' : True,
        'static_path' : os.path.join(os.path.dirname(__file__) , "static") ,
        'template_path' : os.path.join(os.path.dirname(__file__) , "template") ,
    }

    application = tornado.web.Application([
        (r"/" , MainHandler),
    ] , **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


