# C:\Users\张霄港\Desktop\python
import socket
allowClientNumber=10;
serverAddress=(HOST,PORT)="",8888
#创建套接字 
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

#给套接字绑定ip 端口
serverSocket.bind(serverAddress)

serverSocket.listen(allowClientNumber)
print("Server is running on port:",PORT)


while True:
    #接受用户的请求
    client,clientAddress = serverSocket.accept()
    
    request = client.recv(1024)
    print("client 说 :",request)

    sendStr="welcome ..."+clientAddress
    sendStr=sendStr.encode
    # client.send("你好")
    response = b"""\
    HTTP/1.1 200 ok

    hello world
        """;

    client.sendall(response)
    client.close()