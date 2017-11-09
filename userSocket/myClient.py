#C:\Users\张霄港\Desktop\userSocket
import socket
import threading , time

currentUser = "";
def receiveMsg(c , username):
    sendMsg = "login|%s" % username;
    sendMsg = sendMsg.encode();
    c.send(sendMsg);
    while True:
        data = c.recv(1024);
        data = data.decode();
        msgArr = data.split("|");
        if msgArr[0] == "login":
            print("%s 登陆了。。。" % msgArr[1]);
            currentUser = msgArr[1];
        else:
            print(msgArr[0]);

def xxx():
    global currentUser;
    c = socket.socket(socket.AF_INET , socket.SOCK_STREAM);
    c.connect(("127.0.0.1" , 8899));
    username = input("请输入你的名字");

    t = threading.Thread(target=receiveMsg , args=(c , username))
    t.start();

    while True:
        msg = input();
        a = msg.split("--->");
        if len(a) > 1:
            currentUser = a[1];


        if currentUser != "":
            sendMsg = "talk|%s|%s"% (msg , currentUser);
            sendMsg = sendMsg.encode();
            c.send(sendMsg);

    c.close();


if __name__ == "__main__":
    xxx();