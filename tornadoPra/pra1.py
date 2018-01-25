import tornado
import tornado.web

html = '''
<form method="post" name="frm1" action="/login">
    <label for="txt">用户名</label>
    <input type="text" id="txtname" name="myname">
<br/>
<br/>
    <label for="txt">密码  </label>
    <input type="text" id="txtpwd" name="mypwd">
<br/>
<br/>
    <input type="submit">
</form>
'''

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("Hello" + name)

class LoginHandler(BaseHandler):
    def get(self):
        self.write(html)

    def post(self):
        self.set_secure_cookie("user" , self.get_argument("myname"))
        self.redirect("/")

settings = dict(
    cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    login_url = "/login",
    debug = True
)
application = tornado.web.Application([
    (r"/" , MainHandler),
    (r"/login" , LoginHandler)
] , **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()