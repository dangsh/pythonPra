import tornado.web
from uiPra import uimethod as mt, uimodule as md


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("UI.html" , npm="NPM888")

settings = {
    "template_path":"templates",
    "static_path":"statics",
    "ui_methods":mt,
    "ui_modules":md
    # "static_url_prefix":"/statics/" , #前缀
}

application = tornado.web.Application([
    (r"/index" , MainHandler)
] , **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()