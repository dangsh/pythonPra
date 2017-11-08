#C:\Users\张霄港\Desktop\socketDemo1
import socket

c = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# c.bind(("127.0.0.1" , 9999))
c.connect(("127.0.0.1" , 8899))

while True:
    a = input('请输入消息内容:')
    c.send(a.encode())
    # data = c.recv(1024)
    # data = data.decode()
    # print(data)



