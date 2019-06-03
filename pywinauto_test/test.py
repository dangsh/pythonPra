# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 下午2:18
# @Magician  : Dangsh
# When I wrote this , only God and I understood what I was doing
# Now , God only knows


# import sys
# import pywinauto
# import time
# reload(sys)
# sys.setdefaultencoding("utf-8")
#
# app = pywinauto.application.Application()\
#     .start("C:\Users\ceshi\AppData\Roaming\ZoosNet\LiveReception\LiveReception.exe")
from pywinauto.application import Application
import time
# app = Application(backend="uia").start("notepad.exe")
app =  Application(backend="uia").connect(process=17940)
app_window = app.window(class_name = "WindowsForms10.Window.8.app.0.218f99c")
# app_window = app.window(title_re = u".*?网站商务通.*?")

# app_window.children()[1].children()[19].draw_outline(colour = 'red')
app_window.children()[1].children()[18].click()
time.sleep(5)
# history_window = app.window(title_re = u".*?查看历史记录.*?").draw_outline(colour = 'red')
history_window = app.window(title_re = u".*?查看历史记录.*?")
# history_window(auto_id = u"toolStrip1").draw_outline(colour = 'red')
# history_window.children()[4].draw_outline(colour = 'red')
aa = history_window.children()[4]
aa.draw_outline(colour = 'red')
bb = aa.children()[2]
bb.draw_outline(colour = 'green')
# history_window.children()[4].children()[2].draw_outline(colour = 'red')
# history_window.children()[4].children()[2].Select()

history_window.children()[a4].children()[2].children()[1].draw_outline(colour = 'red')
try:
    history_window.children()[4].children()[2].children()[1].select()
except:
    pass
# save


# app.window(auto_id=u"toolStrip1").draw_outline(colour = 'red')
# history_window.children()[3].children()[2].children()[1].click()
# history_window.menu_select(u'导出当前视图->导出到Excel').click()
# history_window[u"导出当前视图"].Click()
# window = app.window_(title_re=u'toolStrip1')
# window.print_control_identifiers()
# bb.menu_select(u'导出当前视图->导出到Excel')
# bb.select()
# ok_window = app.window(title_re = u".*?另存为.*?")
# ok_window.draw_outline(colour = 'red')
# history_window[u'保存(S)'].click()


