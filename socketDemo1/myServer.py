#C:\Users\张霄港\Desktop\socketDemo1
import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.bind(("127.0.0.1" , 8899))

s.listen(5)

print("server is running on 8899")
a = []
chioce = 2 #数组中没有
while True:
    xSock , xAddr = s.accept()
    #判断a数据中有没有xSock这个客户端
    for i in a:
        if i == xSock:
            chioce = 1  #数组中有
    

    if chioce == 1:
       pass

    elif chioce == 2:
        a.append(xSock)

        # print(cSock)
        # print(cAddr)
        # cSock.send("hello sb".encode())

        # data = a[0].recv(1024)
        
        # data = data.decode()
        # data = '客户端说：' + data

        # a[0].send(data.encode())
    for i in a :
        print(i)

        data = i.recv(1024)
        data = data.decode()
        data = '客户端说：' + data
        i.send(data.encode())
        # print(data)
        
s.close()

# <socket.socket fd=576, family=AddressFamily.AF_INET,
#  type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8899), raddr=('127.0.0.1', 65429)>