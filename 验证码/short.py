import json
import re

def getNameTel():
    with open('12_16.json' , encoding='utf-8') as f:
        for i in range(10):
            line = f.readline()
            d = json.loads(line)
            try:
                p=re.compile('^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$')
                match = p.match(d['telephone'][0])
                if match:
                    print(d['lianxiren'][0] , d['telephone'][0])
            except:
                pass
    f.close()