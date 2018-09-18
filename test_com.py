# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(
    host='192.168.14.90',
    port=3306,
    user='root',
    passwd='123456',
    db='hc360',
    charset='utf8'
)
cursor = conn.cursor()
url = "http://zxgaaaa0000001111113344.wx.hc360.com/shop/show.html"
cursor.execute("select * from com_tmp where url = '{}'".format(url))
conn.commit()
result = cursor.fetchone()
if result: 
	print u'不需要爬取'
else:
	print u'爬取并插入数据'
	cursor.execute("insert into com_tmp (url) values ('{}')".format(url))
	conn.commit()
cursor.close()
conn.close()

# if result:
#     print u'存在'
# else:
#     print u'不存在的'