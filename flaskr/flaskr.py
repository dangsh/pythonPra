import os
import sqlite3
from flask import Flask , request , session , g , redirect , url_for , abort , \
    render_template , flash , current_app
from flask_cors import *   

app = Flask(__name__)
CORS(app , supports_credentials=True)



def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(current_app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_db():
    """Initializes the database."""
    with app.app_context():
        db = get_db()
        with current_app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
@app.route("/")
def show_entries():
    cur = g.db.execute('select title, text from entries order by id sesc')
    entries = [dict(title = row[0] , text = row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html' , entries = entries)


@app.route('/add' , methods = ['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title , text) values (? , ?)', [request.form['title'] , request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show entries'))

@app.route('/login' ,methods=['GET' , 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
     # 初始化数据库
    # from contextlib import closing
    # import sqlite3
    # with closing(sqlite3.connect("./myStorage/myDb.db")) as db:
    #     with app.open_resource("schema.sql" , mode = "r") as f:
    #         db.cursor().executescript(f.read())
    #     db.commit()
