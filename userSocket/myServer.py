import socket
import threading , time
import user 

userlist = [];
def noticeAllPeople(px):
    for item in userlist:
        if item.username != px.username:
            item.sendMsg("login|%s" % px.username);
    
    
def sendMsgToOneUser(content , toUser):
    for item in userlist:
        if  item.username == toUser:
            item.sendMsg(content);
    

def yyy(px):
    data = px.recvMsg();
    msgArr = data.split("|");
    print(msgArr);
    if msgArr[0] == "login":
        px.username = msgArr[1];
        print("%s 登陆了" % msgArr[1]);
        noticeAllPeople(px);
    if msgArr[0] == "talk":
        sendMsgToOneUser(msgArr[1] , msgArr[2]);

def xxx():
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM);
    s.bind(("0.0.0.0" , 8899));
    s.listen(5);
    print("服务器允许在" , 8899 , "端口");
    

    while True:
        sock , addr =s.accept();
        px = user.user(sock);
        userlist.append(px);
        t = threading.Thread(target=yyy , args=(px , ));
        t.start();

    s.close();

    


if __name__ == "__main__":
    xxx();