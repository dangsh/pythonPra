import telnetlib


IPPOOL = [{'ipaddr': '180.149.131.67:80'}, {'ipaddr': '211.159.177.212:3128'}, {'ipaddr': '166.111.80.162:3128'}, {'ipaddr': '139.217.24.50:3128'}, {'ipaddr': '220.181.163.231:80'}, {'ipaddr': '202.85.213.220:3128'}, {'ipaddr': '39.134.169.217:8080'}, {'ipaddr': '125.62.26.75:3128'}, {'ipaddr': '124.165.252.72:80'}, {'ipaddr': '112.80.255.21:80'}, {'ipaddr': '121.8.98.197:80'}, {'ipaddr': '183.57.36.87:8888'}, {'ipaddr': '14.215.177.58:80'}, {'ipaddr': '163.177.151.162:80'}, {'ipaddr': '221.7.255.167:80'}, {'ipaddr': '221.7.255.168:80'}, {'ipaddr': '221.7.255.167:8080'}, {'ipaddr': '123.125.115.86:80'}, {'ipaddr': '163.177.151.23:80'}, {'ipaddr': '121.8.98.198:80'}, {'ipaddr': '219.223.251.173:3128'}, {'ipaddr': '61.4.184.180:3128'}, {'ipaddr': '223.112.84.30:3128'}, {'ipaddr': '202.85.213.219:3128'}, {'ipaddr': '222.186.10.29:3128'}, {'ipaddr': '112.80.255.32:80'}, {'ipaddr': '163.177.151.23:80'}, {'ipaddr': '121.8.98.198:80'}, {'ipaddr': '61.4.184.180:3128'}, {'ipaddr': '223.112.84.30:3128'}, {'ipaddr': '202.85.213.219:3128'}, {'ipaddr': '140.143.96.216:80'}, {'ipaddr': '180.97.104.14:80'}]
good_ip = []

for ip in IPPOOL:
     one_ip = ip['ipaddr'] 
     a , b= one_ip.split(':')
     dict = {}
     try:
         telnetlib.Telnet(a, port=b, timeout=1)
         print(one_ip + '  success')
         dict["ipaddr"] = a + ":" + b
         good_ip.append(dict)
     except:
         print(one_ip + ' --------------> error')
print('--------------------------')
print(good_ip)