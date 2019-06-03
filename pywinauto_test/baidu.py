# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 下午5:18
# @Magician  : Dangsh
# When I wrote this , only God and I understood what I was doing
# Now , God only knows

import sys
import pywinauto
from PIL import ImageGrab
from pywinauto import Application,WindowSpecification
from pywinauto.controls.uia_controls import MenuItemWrapper,MenuWrapper
import datetime
import time
import random
import cStringIO
import StringIO
import time
from code_detail import code

reload(sys)
sys.setdefaultencoding("utf-8")

try:
    _ = Application('uia').connect(path=u"C:\Program Files (x86)\\baidu\商桥2016\BaiduBridge.exe")
    _.kill()
except:
    pass
# 启动商务通
app = Application('uia')\
    .start(u"C:\Program Files (x86)\\baidu\商桥2016\BaiduBridge.exe")
window = app.top_window()
time.sleep(2)
username = 'dangsh'
password = '5801200Zxg'
window.print_control_identifiers()

window['Edit2'].type_keys(username)
app.window(auto_id='106385940').draw_outline(colour='red')

