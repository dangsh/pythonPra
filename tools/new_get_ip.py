from flask import Flask
import requests
import json
import time


app = Flask(__name__)

ip = ""
port = ""
arr = []

@app.route("/")
def hello():
    response = requests.get('http://api.xdaili.cn/xdaili-api//newExclusive/getIp?spiderId=f605be9dff0448278c340ee5e6deb0b3&orderno=DX201831487120pKssg&returnType=2&count=1&machineArea=')
    response = json.loads(response.text)
    if response["ERRORCODE"] == "0":
        global ip 
        ip = response["RESULT"][0]["ip"]
        global port
        port = response["RESULT"][0]["port"]
        global arr
        if len(arr) > 50:
            arr = arr[5:]
        arr.append(ip + ":" + port)
    else:
        pass
    return ip + ":" + port

@app.route("/get_arr")
def arrFn():
    response = requests.get('http://api.xdaili.cn/xdaili-api//newExclusive/getIp?spiderId=f605be9dff0448278c340ee5e6deb0b3&orderno=DX201831487120pKssg&returnType=2&count=1&machineArea=')
    response = json.loads(response.text)
    if response["ERRORCODE"] == "0":
        global ip 
        ip = response["RESULT"][0]["ip"]
        global port
        port = response["RESULT"][0]["port"]
        global arr
        if len(arr) > 50:
            arr = arr[5:]
        arr.append(ip + ":" + port)
    else:
        pass
    return str(arr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
