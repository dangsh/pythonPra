# https://passport.baidu.com/v2/api/?login
# https://passport.baidu.com/v2/getpublickey?token=4647fb8d22b56a0c36dba2e9b5e31460&tpl=mn&apiver=v3&tt=1511179299539&gid=36EB853-5B2C-45E8-8716-5A2BD07C090B&traceid=&callback=bd__cbs__vuhaqz
# https://sp1.baidu.com/8qUJcD3n0sgCo2Kml5_Y_D3/v.gif?pid=201&pj=www&fm=behs&tab=tj_login&query=&un=&path=https%3A%2F%2Fwww.baidu.com%2F&wd=&rsv_sid=1469_21103&rsv_did=73a4985f823f21536108fada5ce68ff9&t=1511179673003
import scrapy
from scrapy.spiders import Spider
from scrapy.http import Request
import urllib.request
import urllib.parse
import time
import re
import base64

myHead = {
    "Content-Type":"application/x-www-form-urlencoded",
    "Origin":"https://www.baidu.com",
    "Upgrade-Insecure-Requests":1,
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Connection":"keep-alive" ,
    "Accept-Language" : "zh-CN,zh,1=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Cache-Control":"no-cache" ,
    "Pragma":"no-cache",
    "Host":"www.baidu.com"


}

myHead = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Host":"passport.baidu.com",
    "Pragma":"no-cache",
    "Upgrade-Insecure-Requests":1,
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
 
}

class BaiduScrapy(Spider):
    name = "baidu"
    start_urls = [
        "https://www.baidu.com"
    ]

    def parse(self , response):
        #获取百度首页
       
        request = Request("https://www.baidu.com" , headers = myHead , callback = self.parseHomeFn)
        return request
    
    def parseHomeFn(self , response):
        print("开始解析百度首页")
        if response.status == 200:
            print("开始请求token。。。。。。。。。。。。")
            yield self.getTokenFn()

        else:
            print("请求百度首页出错")
        



    def getFnName(self):
        fnName = "bd__cbs__%d" % time.time()
        print("回调函数name:--------------%s" % fnName)  
        return fnName

    def getGid(self):
        return "54DEF72-683A-4D40-B973-69EE29C92681"

    #token 方法
    def getTokenFn(self):
        baiduTokenUrl = "https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=login&logintype=basicLogin&tt="+"%d"%(time.time() * 1000) + "&callback=" + self.getFnName() + "&gid=" + self.getGid() 
        request = Request(baiduTokenUrl , headers=myHead , callback = self.parseTokenFn)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return request 

        
        # myHead["Host"] = "passport.baidu.com"
        # aaa = "https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=login&logintype=basicLogin"+"&tt="+'%d' % (time.time() * 1000)+"&callback="+self.getFnName()+"&gid="+self.getGid()
        # request = Request(aaa, headers=myHead, callback=self.parseTokenFn)
        # return request
    #解析token的方法
    def parseTokenFn(self , response):
        print("正在解析token值。。。。。。。。。。。。。。。")
        if response.status == 200:
            print("获取token数据成功")

            guize = re.compile('\"token\"\s+:\s+"(\w+)\"')
            mydata = guize.findall(response.body.decode())[0]
            print(mydata)
            self._token = mydata
            yield self.login_history()
        else:
            print("获取token数据失败")

    #获取验证码 和 输入验证

    def login_history(self):
        myHead["Host"] = "passport.baidu.com"
        myHead["Referer"] = "https://passport.baidu.com/v2/?login&u=http://wenku.baidu.com/task/browse/daily"
        myHead["Accept"] = "*/*"
        myHead["Cache-Control"] = "no-cache"
        historyUrl = "https://passport.baidu.com/v2/api/?loginhistory&tpl=pp&apiver=v3&token="+self._token+"&tt="+'%d' % (time.time() * 1000)+"&callback="+self.getFnName()+"&gid="+self.getGid()
        request = Request(historyUrl , headers=myHead , callback=self.parse_login_history_result)
        return request

    def parse_login_history_result(self , response):
        if response.status is 200:
            print("历史登录数据获取成功。。。。")
            yield self.login_check()

        else:
            print("历史登录数据获取失败，httpstatus is" , response.status)

    def login_check(self):
        full_baidu_login_check_url = "https://passport.baidu.com/v2/api/?logincheck&tpl=pp&apiver=v3&sub_source=leadsetpwd&username=18600890116&isphone=false&callback=bd__cbs__u1vvyu&token=" + self._token+"&tt="+'%d' % (time.time() * 1000)+"&callback="+self.getFnName()+"&gid="+self.getGid()
        request = Request(full_baidu_login_check_url , headers=myHead , callback=self.parse_login_check_result)
        return request

    def parse_login_check_result(self , response):
        if response.status is 200:
            print("获取登录检测成功")
            yield self.getpublickey()

        else:
            print("获取登录检测失败")

    def getpublickey(self):
        full_get_public_key_url = "https://passport.baidu.com/v2/getpublickey?tpl=pp&apiver=v3&token=" + self._token+"&tt="+'%d' % (time.time() * 1000)+"&callback="+self.getFnName()+"&gid="+self.getGid()
        request = Request(full_get_public_key_url , headers=myHead , callback=self.parse_get_public_key_result)
        return request

    def parse_get_public_key_result(self , response):
        if response.status is 200:
            
            print("get public key response is" , response.body)
            rsa_key_pattern = re.compile("\"key\"\s*:\s*'(\w+)'")
            match = rsa_key_pattern.search(response.text)
            print("************************************")
            if match:
                rsa_key = match.group(1)
                self._pwd_rsa_key = rsa_key
                print("rsa_key is %s",rsa_key)
            else:
                print("get rsa_key failed!")


            rsa_public_key_pattern = re.compile("\"pubkey\":'(.+?)'")
            match = rsa_public_key_pattern.search(response.text)
            print("************************************")
            if match:
                rsa_public_key = match.group(1)
                rsa_public_key = rsa_public_key.replace('\\n', '\n').replace('\\', '')
                self._pwd_public_rsa_key = rsa_public_key
                print("rsa_public_key is %s", rsa_public_key)
            else:
                print("get rsa_public_key failed!")

            yield self.login()

        else:
            print("获取public key 失败")


    def login(self):
        print("***************************************");
        myHead["Host"] = "passport.baidu.com"
        myHead["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        myHead["Cache-Control"] = "no-cache"
        myHead["Accept-Encoding"] = "gzip, deflate, br"
        myHead["Origin"] = "https://passport.baidu.com"
        myHead["Upgrade-Insecure-Requests"] = 1

        bdData = {
            "staticpage": "https://passport.baidu.com/static/passpc-account/html/v3Jump.html",
            "charset" : "UTF-8",
            "token": self._token,
            "tpl": "pp",  # 重要,需要跟TOKEN_URL中的相同
            "apiver" : "v3",
            "u" : "http://wenku.baidu.com/task/browse/daily",
            "isPhone" : "",
            "safeflg":"0",
            "detect":"1",
            "quick_user":"0",
            "loginmerge":"true",
            "mem_pass":"on",
            "crypttype":"12",
            "logintype" : "basicLogin",
            "logLoginType" : "pc_loginBasic",
            "username": "",
            "password": "",
            "rsakey" : self._pwd_rsa_key,
            "tt": '%d' % (time.time() * 1000),
            'ppui_logintime': 71755,
            'gid': self.getGid(),
            "codeString":"",
            "verifycode":""
        }

        cookies = [{'name': 'FP_UID', 'value': 'a8e078358d61a058b43420dee15e9e77', 'domain': 'baidu.com','path': '/'}]

        #get_user_and_pwd

        # user, password = str(line).strip('\n').split(",")
        bdData["username"] = "itliuxiangyu@163.com"

        # rsakey = RSA.importKey(self._pwd_public_rsa_key)
        # cipher = PKCS1_v1_5.new(rsakey)
        # password = base64.b64encode(cipher.encrypt("sxl2719339"))
        password = base64.encodestring('123456'.encode())
        # s2 = base64.decodestring(s1)
        print("after encrypt, the pwd is %s",password)

        bdData["password"] = password
        postData = urllib.parse.urlencode(bdData).encode("utf-8")
        print("((((((((((((((((((((((((((((((((")
        print("login post data is: %s",postData)
        request = Request("https://passport.baidu.com/v2/api/?login", headers=myHead, cookies=cookies, body=postData, method="POST",callback=self.parse_login_result)
        return request;

    def parse_login_result(self,response):

            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
            print("开始解析登录数据....................");
            if response.status is 200:
                # logging.info("login response is : %s", response.body)
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
                print(response.body.decode())
                # if response.body.find("err_no=0") > -1:
                #     logging.info("login baidu success!")
                # else:
                #     logging.error("login baidu failed")
            else:
                logging.error("post baidu login failed, the httpstatus is: %s", response.status)
