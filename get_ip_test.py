from flask import Flask
import requests
import json
import time
import random
app = Flask(__name__)



@app.route("/")
def hello():
    response = requests.get('http://dev.kuaidaili.com/api/getproxy/?orderid=922453937034843&num=10&area=%E4%B8%AD%E5%9B%BD&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=2&method=2&an_an=1&an_ha=1&sp1=1&quality=1&sort=1&format=json&sep=1')
    response = json.loads(response.text)
    
    if response['code'] == 0:
        global ips
        ips = str(random.choice(response['data']['proxy_list']))
        print(ips)
    else:
        pass
    return ips
if __name__ == '__main__':
    ips = ""
    print(ips)
    app.run(host='0.0.0.0', port=7777, debug=True)
