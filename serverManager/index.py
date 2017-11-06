from flask import Flask , request , \
send_from_directory , url_for , render_template , redirect  , g

from werkzeug import secure_filename
import json
from contextlib import closing
import sqlite3

from flask_cors import *

app = Flask(__name__)

CORS(app , supports_credentials=True)
@app.route("/")
def indexFn():
    return "我是index 界面"

@app.route("/uploadFile" , methods = ["POST"])
def uploadFileFn():
    if request.method == "POST":
        f = request.files["sb"]
        # print(f)
        f.save("./uploadFile/" + secure_filename(f.filename))
        return "服务器收到文件"
    else:
        return "请用POST访问该地址"

@app.route("/xxx")
def xxxFn():
    return redirect(url_for("yyyFn"))


@app.route("/yyy")
def yyyFn():
    return "yyy"


@app.route("/login" , methods=["GET" , "POST"])
def loginFn():
    if request.method == "GET":
        return render_template("login.html")

    else:
        #post请求   要判断用户名密码
        userName = request.form["username"]
        passWord = request.form["password"]
        #遍历数据库中的数据 看有没有该用户名和密码

        sqlStr ="select username , password from userTable"
        userTableResult = g.db.execute(sqlStr)
        userTableData = [dict(username = row[0] , password = row[1]) for row in userTableResult.fetchall()]

        isHaveThisUser = False
        thisItem = None

        for item in userTableData:
            if str(item["username"]) == userName:
                isHaveThisUser = True;
                thisItem = item
                break;
        if isHaveThisUser == False:
            return "用户名不存在"
        else:
            if str(thisItem["password"]) != passWord:
                return "密码错误"
            else:
                return redirect(url_for("homeFn"))



@app.route("/register" , methods=["GET" , "POST"])
def registerFn():
    if request.method == "GET":
        return render_template("register.html")

    else:
        userName = request.form["username"]
        passWord = request.form["password"]
        sqlStr = "insert into userTable (username ,password) values ('%s' , '%s')" % (userName , passWord)
        g.db.execute(sqlStr)
        g.db.commit()
        return redirect(url_for("loginFn"))
    
#home 路由
@app.route("/home")
def homeFn():
    return render_template("home.html")


# 访问服务器资源
@app.route("/serverFile/<filename>")
def serverFileFn(filename):
    return send_from_directory("./uploadFile/" , filename)


@app.errorhandler(404)
def lostPage(err):
    return render_template("lostPage.html")
    # return redirect(url_for("indexFn"))

#页面请求之前
@app.before_request
def before_requestFn():
    g.db = sqlite3.connect("./myStorage/myDb.db")


#页面请求之后
@app.teardown_request
def teardown_requestFn(a):
    g.db.close()

#展示商品列表
@app.route("/showProducts")
def showProductsFn():
    sqlStr ="select productname , shop , freight , norm , price1 , productdepict , aftersale , depictandimage , id , imgurl from productTable"
    listResult = g.db.execute(sqlStr)
    listData = [dict(productname = row[0] , shop = row[1] ,freight = row[2] , norm = row[3] ,price1 = row[4] , productdepict = row[5] ,aftersale = row[6] , depictandimage = row[7] , id = row[8] , imgurl = row[9]) for row in listResult.fetchall()]
    return json.dumps({"data":listData})

#添加商品
@app.route("/addProduct" , methods=["POST"])
def addProductFn():

    productname = request.form["productname"]
    shop = request.form["shop"]
    freight = request.form["freight"]
    norm = request.form["norm"]
    price1 = request.form["price1"]
    productdepict = request.form["productdepict"]
    aftersale = request.form["aftersale"]
    depictandimage = request.form["depictandimage"]

    image = request.files["image"]
    image.save("./uploadFile/" + secure_filename(image.filename))



    sqlStr = "insert into productTable (productname , shop , freight , norm , price1 , productdepict , aftersale , depictandimage , imgurl)  values ('%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s')" % (productname , shop , freight , norm , price1 , productdepict , aftersale , depictandimage , image.filename)
    g.db.execute(sqlStr)
    g.db.commit()

    return json.dumps({"msg" : "tijiaochenggongxxx"})

#delete 根据id删除商品
@app.route("/delete" , methods=["POST"])
def deleteFn():
    productId = request.values.get("id");

    sqlStr = "delete from productTable where id ='%s' " % str(productId);
    g.db.execute(sqlStr);
    g.db.commit();


    return json.dumps({"msg" : productId })


if __name__ == "__main__":
    app.run()



    # 初始化数据库
    # from contextlib import closing
    # import sqlite3
    # with closing(sqlite3.connect("./myStorage/myDb.db")) as db:
    #     with app.open_resource("./myStorage/mySql.sql" , mode = "r") as f:
    #         db.cursor().executescript(f.read())
    #     db.commit()