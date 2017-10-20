import pymysql.cursors

conn  = pymysql.Connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="5801200zxg",
    db="python",
    charset="utf8"

);


#handel
cursor = conn.cursor();

# sql="create database python"
# cursor.execute(sql);

# sql="create table Student(name varchar(10) not null primary key ,age int(3) not null ,sex varchar(4) not null,datetime timestamp)";
# cursor.execute(sql);

sql="insert into Student (name,age,sex) values ('lisi',13,'nan')";
cursor.execute(sql);
conn.commit();

sql="select * from Student";
cursor.execute(sql);
for row in cursor.fetchall():
    print(row);