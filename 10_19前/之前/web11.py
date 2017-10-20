# C:\Users\张霄港\Desktop\python
import web

urls=(
    '/(.*)','xxx'


);

render=web.template.render("templates/")

class xxx:
    def GET(self,name):
        if name=="":
            name="jjj"
        # return "<h1>hhhhhh</h1>";
        # a = web.input(name=None);
        return render.hello(name);

if __name__ == "__main__":
    app = web.application(urls , globals());
    app.run();