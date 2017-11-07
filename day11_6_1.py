from flask import Flask , request , \
send_from_directory , url_for , render_template , redirect , g
from werkzeug import secure_filename
import json 
from contextlib import closing
import sqlite3
from flask_cors import *

app =Flask(__name__)
CORS(app , supports_credentials =True)

@app.route("/uploadFile" , methods = ["POST"])
def uploadFileFn():
    if request.method == "POST":
        f = request.files["sb"]
        f.save("./uploadFile/" + secure_filename(f.filename))
        return "服务器收到文件"
    else:
        return "请用post访问该地址"

@app.route("/register" , methods = ["GET" , "POST"])
def registerFn():
    if request.method == "GET":

        return render_template("register.html")
    else :
        userName = request.form["username"]
        password = request.form["password"]
        sqlStr = "insert into userTable (username , password ) values ('%s' , '%s') " % (userName , password)
        g.db.execute(sqlStr)
        g.db.commit()
        return redirect(url_for("loginFn"))

@app.route("/login" , methods = ["GET" , "POST"])
def loginFn():
    if request.method == "GET":
        return render_template("login.html")
    else :
        userName = request.form["username"]
        password = request.form["password"]

        sqlStr = "select username , password from userTable"
        userTableResult = g.db.execute(sqlStr)
        userTableData = [dict(username = row[0] , password = row[1]) for row in userTableResult.fetchall()]
        
        for i in userTableData:
            if str(i["username"]) == userName:
                if set(i["password"]) == password:
                    return redirect(url_for("homeFn"))
                else:
                    return "密码错误"
            else:
                return "账号错误"
        return "登录失败"


@app.errorhandler(404)
def lostPage(err):
    return render_template("lostPage.html")

#访问服务器资源
@app.route("/serverFile/<filename>")
def serverFileFn(filename):
    return send_from_directory("./uploadFile/" , filename)

#页面请求之前
@app.before_request
def before_requestFn():
    g.db = sqlite3.connect("./myStorage/myDb.db")

#页面请求之后
@app.teardown_request
def teardown_request(a):
    g.db.close()

#添加商品        
@app.route("/addProduct" , methods=["POST"])
def addProductFn():
    productname = request.form["productname"]
    shop =request.form["shop"]
    freight = request.form["freight"]
    norm = request.form["norm"]
    price = request.form["pricr"]
    productdepict = request.form["productdepict"]
    aftersale = request.form["aftersale"]
    depictandimage = request.form["depictandimage"]
    image = request.files["image"]
    image.save("./uploadFile/" + secure_filename(image.filename))
    sqlStr = "insert into productTable ( productname , shop , freight ,norm ) values ('%s' , '%s' , '%s' , '%s' )" % (productname)
    g.db.execute(sqlStr)
    g.db.commit()
    return json.dumps({"msg" : "tijaiochenggong"})

#展示商品列表
@app.route("/showProducts")
def showProductsFn():
    sqlStr = "select productname from productTable"
    listResult = g.db.execute(sqlStr)
    listData = [dict(productname = row[0]) for row in listResult.fetchall()]
    return json.dumps({"data" : listData})

#根据id删除商品
@app.route("/delete" , methods = ["POST"])
def deleteFn():
    productId = request.values.get("id")
    sqlStr = "delete from productTable where id = '%s' " % str(productId)
    g.db.execute(sqlStr)
    g.db.commit()


if __name__ = "__main__" :
    app.run()



#初始化数据库

from contextlib import closing
import sqlite3
with closing(sqlite3.connect("./myStorage/myDb.db")) as db:
    with app.open_resource("./myStorage/mySql.sql" , mode = "r") as f:
        db.cursor().executescript(f.read())
    db.close()