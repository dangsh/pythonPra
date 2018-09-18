import pymysql

 
#打开数据库连接
db = pymysql.connect(host="172.20.10.9",port=3306,user="info",passwd='info895316',db="info",charset="utf8")
#使用cursor()方法获取游标对象
cursor= db.cursor()
for i in range(50):
    # sql = "CREATE TABLE info_keyword_%s (id  bigint NOT NULL ,keyword  varchar(100) NULL unique ,zids  varchar(2500) NULL DEFAULT '' ,PRIMARY KEY (id));" %(str(i),)
    # sql = "DROP TABLE if exists info_keyword%s "%(str(i),)
    sql = "CREATE TABLE info_detail_%s (zid bigint(20) NOT NULL,cate1_id int(11) DEFAULT '0',cate2_id int(11) DEFAULT '0',industry_id int(11) DEFAULT '0',title varchar(50) DEFAULT NULL, `desc` text ,source varchar(50) DEFAULT NULL,source_url varchar(150) DEFAULT NULL,keywords varchar(100) DEFAULT NULL,abstract text,status int(11) DEFAULT '0',addtime bigint(20) DEFAULT '0',PRIMARY KEY (zid));" %(str(i),)
    cursor.execute(sql)
db.close()