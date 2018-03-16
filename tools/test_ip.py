import telnetlib


IPPOOL = [{'ipaddr': '211.159.177.212:3128'}, {'ipaddr': '166.111.80.162:3128'}, {'ipaddr': '120.77.254.116:3128'}, {'ipaddr': '139.217.24.50:3128'}, {'ipaddr': '124.165.252.72:80'}, {'ipaddr': '124.165.252.72:8081'}, {'ipaddr': '119.27.177.169:80'}, {'ipaddr': '121.8.98.197:80'}, {'ipaddr': '121.8.98.198:80'}, {'ipaddr': '61.4.184.180:3128'}, {'ipaddr': '121.8.98.198:80'}, {'ipaddr': '61.4.184.180:3128'}, {'ipaddr': '61.136.163.245:8104'}, {'ipaddr': '61.136.163.245:3128'}, {'ipaddr': '61.136.163.245:3128'}, {'ipaddr': '61.136.163.245:8104'}]
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