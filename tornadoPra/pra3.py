import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form>'
                   '<form action="/story/1" method="get">'
                   '<input type="submit" value="aaa">'
                   '</form></body></html>')
    def post(self):
        self.set_header("Content-Type" , "text/plain")
        self.write("You wrote " + self.get_argument("message"))


class StoryHandler(tornado.web.RequestHandler):
    def get(self , story_id):
        self.write("you requested the story " + story_id)

class RedHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('/' , permanent=True)

application = tornado.web.Application([
    (r"/" , MainHandler),
    (r"/story/([0-9]+)" , StoryHandler),
    (r"/redirect" , RedHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()