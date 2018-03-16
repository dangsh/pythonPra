import time , json , requests
t = time.time()
while True:
    new_t = time.time()
    if int(t) + 17 <= int(new_t):
        response = requests.get('http://api.xdaili.cn/xdaili-api//newExclusive/getIp?spiderId=f605be9dff0448278c340ee5e6deb0b3&orderno=DX201831487120pKssg&returnType=2&count=1&machineArea=')
        response = json.loads(response.text)
        ip = response["RESULT"][0]["ip"]
        port = response["RESULT"][0]["port"]
        print("this ip is " + ip + ":" + port)
        t = time.time()
    else:
        pass