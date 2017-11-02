from flask import Flask , request , render_template , g
import sqlite3
from contextlib import closing

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/register" , methods = ["GET" , "POST"])
def registerFn():
	return "success"

app.run()
