# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 下午2:24
# @Magician  : Dangsh
# When I wrote this , only God and I understood what I was doing
# Now , God only knows


from pywinauto.application import Application
import pywinauto
import time
import datetime
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


site_id = 'LRW77021783'
username = 'chenkeyi'

swt_app = Application('uia').connect(title_re=u"网站商务通.+?%s.+%s" % (site_id , username))
# main_w = swt_app.window(title_re=u"网站商务通.+?%s.+" % site_id)

history_window = swt_app.window(title_re=u"网站商务通.+查看历史记录")
history_window.draw_outline(colour = 'red')
now_date = datetime.datetime.now()
yesterday = now_date - datetime.timedelta(days=1)
print yesterday
y , m , d = yesterday.strftime("%Y-%m-%d").split("-")
# 期望效果  2019年05月27日 00:00:00Custom
now_date_format = now_date.strftime(u"%Y年%m月%d日 00:00:00Custom").decode('utf-8')
yesterday_format = yesterday.strftime(u"%Y年%m月%d日 00:00:00Custom").decode('utf-8')
print now_date_format
print yesterday_format
time_bar = history_window[now_date_format]
time_bar.draw_outline(colour='red')
time.sleep(1)
a = time_bar.rectangle()
left = a.left
top = a.top
print "left" , a.left
print "top" , a.top
pywinauto.mouse.click(button='left' , coords=(left +5 , top))
# pywinauto.keyboard.send_keys("1"
#                              "{VK_SPACE}"
#                              "2"
#                              "{VK_SPACE}"
#                              d
#                              )
pywinauto.keyboard.send_keys("%s{VK_SPACE}%s{VK_SPACE}%s"%(y,m,d))
history_window[u'刷新Button'].click()
# history_window.print_control_identifiers()


# time_bar.set_time(2001, 1, 1)
# date_time_picker = get_child_by_properties(time_bar, {'class_name': 'SysDateTimePick32', 'control_id': ur control nr})
# date_time_picker.set_time(date_time.year, date_time.month, date_time.weekday(), date_time.day, date_time.hour, date_time.minute, date_time.second, date_time.microsecond)


# a = history_window.window(class_name='"WindowsForms10.SysDateTimePick32.app.0.33c0d9d')
# a.draw_outline(colour='blue')