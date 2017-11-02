from flask import Flask , request , render_template , g
import sqlite3
from contextlib import closing

app = Flask(__name__)
app.config.from_object(__name__)

"""登录时间的路由"""
@app.route("/login" , methods = ["GET" , "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		username1 = request.form["username"]
		password1 = request.form["password"]
		mysql = "select username , password from userTable"
		result = g.db.execute(mysql)
		aaa = [dict(username=row[0] , password = row[1]) for row in result.fetchall()]

		print(aaa)
		for i in aaa:
			if str(i["username"]) == username1:
				if str(i["password"]) == password1:
					return "login success"
				else:
					return "password error"
		return "username error"
"""注册路由"""
@app.route("/register" , methods = ["GET" , "POST"])
def registerFn():
	if request.method == "GET":
		return render_template("register.html")
	else:
		username = request.form["username"]
		password = request.form["password"]
		pasword = str(password)

		g.db.execute("insert into userTable(username , password) values(? , ?)" , [username , password])
		g.db.commit()
		return "you name is: " + username + "you password id: " + password


"""连接数据库方法"""
def connec_db():
	return sqlite3.connect("database/mydb.db")

"""初始化数据库方法"""
def init_db():
	with closing(connec_db()) as db:
		with app.open_resource("sql.sql" ,mode = 'r') as f:
			db.cursor().executescript(f.read())
		db.commit()

# init_db()

@app.before_request
def before_requestFn():
	#链接数据库
	g.db = connec_db()

@app.teardown_request
def teardown_requestFn(a):
	#关闭数据库
	g.db.close()

app.run()
