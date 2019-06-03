# coding:utf-8
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


try:
    _ = Application('uia').connect(path="C:\Users\ceshi\AppData\Roaming\ZoosNet\LiveReception\LiveReception.exe")
    _.kill()
except:
    pass
# 启动商务通
app = Application('uia')\
    .start("C:\Users\ceshi\AppData\Roaming\ZoosNet\LiveReception\LiveReception.exe")
window = app.top_window()
time.sleep(1)
# 输入账号密码，点击登录
site_id = 'LRW77021783'
username = 'chenkeyi'
password = 'Xz7232275'
output_file_name = 'output.xls'
window['Edit4'].type_keys(site_id)
window['Edit2'].type_keys(username)
window['Edit1'].type_keys(password)
window['Button5'].click()
# 延时5秒，等待商务通返回登录的结果
time.sleep(6)
while True:
    time.sleep(3)
    try:
        swt_app = Application('uia').connect(title_re=u"网站商务通.+?%s.+" % site_id)
        break
    except:
        # 没有发现业务进程，说明登录进程尚未结束，可能需要再次进入登录逻辑
        try:
            # 验证码逻辑
            vertify_window = app.window(top_level_only=False, title=u'登录验证')
            assert vertify_window.exists()
            print "出现验证码"
            pic_name = str(int(time.time())) + '.jpg'
            grab_window(vertify_window , pic_name)
            auth_code =  code(pic_name)
            a = vertify_window.window(title=u"为了您的账号安全，本次登录需输验证码。" , found_index = 0)
            a.draw_outline(colour='red')
            a.type_keys(auth_code)
            vertify_window.window(title = u"确定").click()
            continue
        except Exception as e:
            print e
        my_window = app.top_window()
        try:
            error_password_window = my_window.window(title=u"您输入的密码不正确！")
            error_password_window.draw_outline(colour='blue')
            print "密码错误"
            my_window.window(title = u"确定").click()
            break
        except Exception as e:
            print e
            pass

        try:
            my_window.window(title=u"微信验证")
            print "需要微信验证"
            break
        except:
            pass


print u"已捕获到主功能窗口，进入主逻辑"
time.sleep(1)
main_w = swt_app.window(title_re=u"网站商务通.+?%s.+" % site_id)
now_date = datetime.datetime.now()
yesterday = now_date - datetime.timedelta(days=1)
y, m, d = yesterday.strftime("%Y-%m-%d").split("-")
# 期望效果  2019年05月27日 00:00:00Custom
now_date_format = now_date.strftime(u"%Y年%m月%d日 00:00:00Custom").decode('utf-8')
yesterday_format = yesterday.strftime(u"%Y年%m月%d日 00:00:00Custom").decode('utf-8')


for i in range(50):
    print u"尝试打开历史记录窗口..."
    try:
        history_btn = main_w.window(title=u'历史记录')
        _ = history_btn.exists()
        assert _
    except Exception as e:
        main_w = swt_app.window(title_re=u"网站商务通.+?%s.+" % site_id)
    else:
        history_window = None
        for j in range(50):
            # 多次点击 防止点不上
            history_btn.click()
            time.sleep(0.5)
            history_window = swt_app.window(title_re=u"网站商务通.+查看历史记录")
            time.sleep(15)   # 等待加载完成
            if history_window.exists():
                print u"历史记录窗口已打开"
                break
        if history_window:
            tool_strip_3 = history_window.window(title=u'toolStrip3', found_index=0)
            # 尝试调出设置窗口
            try:
                history_window[u'\u81ea\u5b9a\u4e49\u62a5\u8868MenuItem'].select()
                history_window[u'\u81ea\u5b9a\u4e49\u62a5\u8868MenuItem'].select()
                history_window[u'\u81ea\u5b9a\u4e49\u62a5\u8868MenuItem'].select()
                history_window[u'\u81ea\u5b9a\u4e49\u62a5\u8868MenuItem'].select()
            except:
                pass
            time.sleep(0.4)
            if not history_window[u'恢复默认Button'].exists():
                print u"打开设置报表窗口失败"
            else:
                history_window[u'恢复默认Button'].click()
                time.sleep(0.3)
                pop_window = history_window.window(title=u"恢复默认设置提示") # ['Button1'].click()
                ok_btn = pop_window.child_window(title=u'确定')
                ok_btn.click()
                history_window[u'修改Button'].click()
                history_window[u'全选Button'].click()
                history_window[u'确定Button'].click()
                try:
                    history_window[u'全部记录报表MenuItem'].select()
                    history_window[u'全部记录报表MenuItem'].select()
                    history_window[u'全部记录报表MenuItem'].select()
                except:
                    pass
                history_window.window(title=u'设置常用报表').close()
                # 设置时间 ，昨天0：00 到当前时间

                time_bar = history_window[now_date_format]
                time_bar.draw_outline(colour='red')
                time.sleep(1)
                a = time_bar.rectangle()
                left = a.left
                top = a.top
                pywinauto.mouse.click(button='left', coords=(left + 5, top))
                pywinauto.keyboard.send_keys("%s{VK_SPACE}%s{VK_SPACE}%s" % (y, m, d))
                history_window[u'刷新Button'].click()
                time.sleep(15)
                history_window[u'导出到ExcelMenuItem'].select()
                time.sleep(0.5)
                save_window = history_window.window(title=u'另存为')
                # save_window.print_control_identifiers()
                save_window.window(best_match=u'Edit11').type_keys(output_file_name)
                save_window.window(best_match=u'\u4fdd\u5b58(S)Button').click()
                time.sleep(0.5)
                # 覆盖文件判断
                _ = history_window.window(title=u'确认另存为')
                if _.exists():
                    _.window(best_match=u'是(Y)Button').click()
                time.sleep(5)  # 等待导出完成
                break
        else:
            print u"无法打开历史窗口， 程序错误。"

    time.sleep(1)

else:
    print u"系统异常，无法获取到主功能窗口"
swt_app.kill()


# import datetime
#
# now_date = datetime.datetime.now()
# yesterday = now_date - datetime.timedelta(days=1)
# # 期望效果  2019年05月27日 00:00:00Custom
# yesterday_format = yesterday.strftime("%Y年%m月%d日 00:00:00Custom").decode('utf-8')