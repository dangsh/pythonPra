import re
import json, urllib
from urllib.parse import urlencode
import urllib.request
from short import getNameTel

#发送短信接口  测试用  （陈云飞）
def shortMsgFromPhone():
    phone = "18538749356"
    p=re.compile('^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$')
    match = p.match(phone)
    if match:
        sendurl = 'http://v.juhe.cn/sms/send' #短信发送的URL,无需修改 
        appkey = '0f2f46d95cfe854988012bf5a1da65cf';
        mobile = phone;
        tpl_id = "56951";
        code = "GETqeU904d";
        tpl_value = '#code#='+code;
        params = 'key=%s&mobile=%s&tpl_id=%s&tpl_value=%s' % \
        (appkey, mobile, tpl_id, urllib.request.quote(tpl_value)) #组合参数
            
        wp =urllib.request.urlopen(sendurl+"?"+params)
        content = wp.read() #获取接口返回内容
            
        result = json.loads(content)
        error_code = result['error_code']
        if error_code == 0:
            #发送成功
            smsid = result['result']['sid']
            statusDic = {"status":"ok" , "smsid":smsid}
            print(statusDic)
        else: 
            #发送失败
            statusDic = {"status":"error" , "reason":result['reason']}
            print(statusDic)
    else:
        pass


# shortMsgFromPhone();
getNameTel()