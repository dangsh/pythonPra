import os
import tornado.ioloop
import tornado.web
from settings import db

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class WeiboHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        return self.render("weibo_add.html")
    
    @tornado.web.authenticated
    def post(self):
        result = self.get_argument("content" , "")
        db.weibo.insert({"content":result,"user":self.get_current_user()})
        self.write(result)

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("hello  " + name)

class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                    'Name:<input type="text" name="name">'
                    '<input type="submit" value="Sign in ">'
                    '</form></body></html>' )
    
    def post(self):
        self.set_secure_cookie("user" , self.get_argument("name"))
        self.redirect("/")

settings = {
    "cookie_secret" : "asdfghjklzxcvbnm/Vo=",
    "login_url" : "/login",
    "template_path" : os.path.join(os.path.dirname(__file__) , "templates"),
    "debug":True
}
application = tornado.web.Application([
    (r"/" , MainHandler) ,
    (r"/login" , LoginHandler) ,
    (r"/weibo/add" , WeiboHandler) ,
] , **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
