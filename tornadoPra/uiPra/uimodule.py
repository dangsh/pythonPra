from tornado.web import UIModule

class talk(UIModule):
    def render(self , name):
        return "Have a good day " + name