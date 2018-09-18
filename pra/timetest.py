import time


# proxy = '192.168.14.12%s:3128'%my_time
# print proxy
for i in range(100):
    my_time = time.localtime()[5]
    my_time = str(my_time)
    if len(my_time) == 1:
        my_time = '0' + my_time
    proxy_code = my_time[0]
    proxy = '192.168.14.12%s:3128' % proxy_code
    print my_time , proxy
    time.sleep(1)