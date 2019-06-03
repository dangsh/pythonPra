# coding:utf-8
import sys
import pywinauto
from PIL import ImageGrab
from pywinauto import Application,WindowSpecification
import time
import random
import cStringIO
import StringIO

reload(sys)
sys.setdefaultencoding("utf-8")


def grab_window(window_object, image):
    '''把一个window对象截图(JPEG)
    如果image是一个对象，比如是一个StringIo类型的对象，本函数会把图片内容写入到对象中
    如果image是一个str，比如：aa.png 本函数会把图片写入到该文件中
    返回值：
    None
    '''
    a = window_object.rectangle()
    vertify_image = ImageGrab.grab((a.left, a.top,
                                    a.left+a.width(),
                                    a.top+a.height()))
    if isinstance(image, StringIO.StringIO) or 'StringIO' in str(type(image)):
        vertify_image.save(image, quality=100, format='JPEG')
    elif isinstance(image, (str,unicode)):
        vertify_image.save(image, quality=100, format='JPEG')


# 启动商务通
app = Application('uia')\
    .start("C:\Users\ceshi\AppData\Roaming\ZoosNet\LiveReception\LiveReception.exe")
# window = app.top_window()
window = app.window(auto_id = "LoginFrm_New")
time.sleep(1)
# 输入账号密码，点击登录
site_id = 'LRW77021783'
username = 'chenkeyi'
password = 'Xz7232275'
window['Edit4'].type_keys(site_id)
window['Edit2'].type_keys(username)
window['Edit1'].type_keys(password)
window['Button5'].click()
# 延时5秒，等待商务通返回登录的结果
time.sleep(6)
swt_app = Application('uia').connect(title_re=u"网站商务通.+?%s.+" % site_id
                                     )
if not swt_app.is_process_running():
    # 登录进程尚未结束，可能需要再次进入登录逻辑
    try:
        # 验证码逻辑
        vertify_window = app.window(top_level_only=False, title=u'登录验证')
        assert vertify_window.exists()
        print vertify_window.print_control_identifiers()
        a = vertify_window['Pane']
        vertify_img_f = cStringIO.StringIO()
        grab_window(a, vertify_img_f)
        print vertify_img_f.getvalue()
    except:
        try:
            # 密码错误逻辑
            error_password_window = app.window(top_level_only=False, title=u"您输入的密码不正确!")
            assert error_password_window.exists()
            print "账号或者密码不正确"
        except:
            pass
else:
    # 登录进程结束.进入主逻辑
    print u"已捕获到主功能窗口"
    time.sleep(1)
    main_w = swt_app.window(title_re=u"网站商务通.+?%s.+" % site_id)
    for i in range(50):
        print u"尝试打开历史记录窗口..."
        try:
            history_w = main_w.window(title=u'历史记录')
            _ = history_w.exists()
            assert _
        except Exception as e:
            main_w = swt_app.window(title_re=u"网站商务通.+?%s.+" % site_id)
        else:
            for j in range(50):
                # 多次点击 防止点不上
                history_w.click()
                time.sleep(0.5)
                history_window = swt_app.window(title_re=u"网站商务通.+查看历史记录")
                time.sleep(5)
                if history_window.exists():
                    print u"历史记录窗口已打开"
                    a = history_window.window(title=u'全部记录报表',found_index=0)
                    a.draw_outline(colour = 'red')
                    a.select()

                    b = history_window.window(title=u'自定义报表')
                    b.draw_outline(colour = 'green')
                    b.select()

                    c = history_window.window(title=u'恢复默认')
                    c.draw_outline(colour = 'yellow')
                    c.click()

                    d = history_window.window(title=u'确定')
                    d.draw_outline(colour='yellow')
                    d.click()

                    e = history_window.window(title=u'修改')
                    e.draw_outline(colour='yellow')
                    e.click()

                    f = history_window.window(title=u'全选')
                    f.draw_outline(colour='yellow')
                    f.click()

                    g = history_window.window(title=u'确定')
                    g.draw_outline(colour='yellow')
                    g.click()

                    h = history_window.window(title=u'设置常用报表')
                    h.draw_outline(colour='red')
                    h.close()


                    # b = a.wrapper_object()
                    # print b
                    # a.print_ctrl_ids()
                    # print a.items()
                    # a.select(u"自定义")
                    # history_window.windows(title=u'全部记录报表').wrapper_object().click()
                    time.sleep(5)
                    break
            break
        time.sleep(1)

    else:
        print u"系统异常，无法获取到主功能窗口"
    # swt_app.kill()

