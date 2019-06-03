# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 上午11:39
# @Magician  : Dangsh
# When I wrote this , only God and I understood what I was doing
# Now , God only knows

import os
import requests
url = "https://qiniu-xpc0.xpccdn.com/5c3d41b469da0.mp4"
response = requests.get(url , stream=True)
with open("test.mp4" , 'wb') as file:
    file.write(response.content)
