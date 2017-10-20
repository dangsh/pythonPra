import socket
import tkinter
from wxpy import *
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM);

#开始连接服务器
client.connect(("192.168.7.116",8888));
#发送数据
client.send(b"aaaaaaaaaaaaaaaaaaaaaaaaa");


data = client.recv(1024);
print(data.decode());
mainloop()