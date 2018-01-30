import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello , World')

class CmdbHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Cmdb')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('3.html')

settings = {
    'template_path' : 'templates' ,
}
application = tornado.web.Application([
    (r'/main' , MainHandler) ,
    (r'/index' , IndexHandler) ,
] , **settings)

#添加二级域名
application.add_handlers('cmdb.fuzengjie.cn' , [
    (r'/main' , CmdbHandler)
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()