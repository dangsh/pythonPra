import socket

class user:
    def __init__(self , sot , username = "kong"):
        self.username = username ;
        self.sot = sot ;

    def sendMsg(self , msg):
        self.sot.send(msg.encode())


    def recvMsg(self):
        data = self.sot.recv(1024);
        data = data.decode();
        return data;
