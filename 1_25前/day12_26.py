#b站发弹幕
import requests
import time
import configparser #配置文件

target = configparser.ConfigParser()
target.read(r'D:\pythonPra\ssg.ini')
print(target['aaa']['1'])

# url = 'https://interface.bilibili.com/dmpost?cid=26977466&aid=16538656&pid=1&ct=1'

# cookie = {
#     'Cookie':"buvid3=A28E32D3-E430-44A7-9818-B98B1855A3DE38847infoc; finger=964b42c0; LIVE_BUVID=AUTO2615137693293420; fts=1514291263; sid=bqj9pkms; purl_token=bilibili_1514291277; UM_distinctid=16092cb3c3a9-066400fbc379858-12676c4a-1fa400-16092cb3c3b2e7; pgv_pvi=8878124032; pgv_si=s6269020160; DedeUserID=5723630; DedeUserID__ckMd5=70f41e80a3aeb82b; SESSDATA=8d19b513%2C1516883327%2Ccb254420; bili_jct=4da9100e2f37bbb5799939739aa7b1ea; _dfcaptcha=3155b4943f2b1f0aeff21410c56fe290; _cnt_pm=0; _cnt_notify=4"
# }

# form = {
# 'fontsize':'25',
# 'pool':'0',
# 'mode':'1',
# 'color':'16777215',
# 'rnd':str(time.time()*1000000),
# 'message':'我用py',
# 'playTime':'0.08',
# 'cid':'26977466',
# 'date':time.strftime("%Y-%m-%d+%X",time.localtime()),
# 'csrf':'4da9100e2f37bbb5799939739aa7b1ea',
# }
# requests.request('POST' , url , data=form , cookies = cookie) 