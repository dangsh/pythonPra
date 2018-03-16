# import time , os
# def re_exe(cmd , inc=10):
# 	while True:
# 		os.system(cmd)
# 		time.sleep(inc)

# re_exe("echo %time%" , 5)

import time , requests , json ,threading

def getIP():
	while True:
	    response = requests.get('http://api.xdaili.cn/xdaili-api//newExclusive/getIp?spiderId=f605be9dff0448278c340ee5e6deb0b3&orderno=DX201831487120pKssg&returnType=2&count=1&machineArea=')
	    response = json.loads(response.text)
	    ip = response["RESULT"][0]["ip"]
	    port = response["RESULT"][0]["port"]
	    print("this ip is " + ip + ":" + port)
	    time.sleep(17)

def console():
	while True:
		print("a")
		time.sleep(1)

if __name__ == "__main__":
	t1 = threading.Thread(target=getIP)
	t2 = threading.Thread(target=console)
	t1.start()
	t2.start()
	t1.join()
	t2.join()

	
