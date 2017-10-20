from tkinter import *
from wxpy import *
class WidgetsDemo:
   
    # 初始化机器人，扫码登陆
    bot = Bot(cache_path=True);
    def __init__(self):
        master=Tk()
        master.title("微信聊天")

        self.name=StringVar()
        labal1=Label(master, text="名称")
        e1=Entry(master,textvariable=self.name)
        labal1.pack();
        e1.pack();
        sendBtn=Button(master,text="搜索姓名",command=self.searchFn)
        sendBtn.pack();

        self.name2=StringVar()
        labal2=Label(master, text="信息")
        e2=Entry(master,textvariable=self.name2)
        labal2.pack();
        e2.pack();
        sendBtn2=Button(master,text="发送信息",command=self.sendFn)
        sendBtn2.pack();

        mainloop()

    def printname(self):#信息可以获取成功

        print("你的名字是："+self.name.get())
        print("发送的信息是"+self.name2.get())
    def searchFn(self):
        self.toUser=self.bot.friends().search(self.name.get())[0];
    def sendFn(self):
        sendMsg=self.name2.get();
        self.toUser.send(sendMsg);


    '''
    # 初始化机器人，扫码登陆
    bot = Bot(cache_path=True);

    
   

    my_friend = bot.friends().search('李丹阳')[0]
    print(my_friend)
    my_friend.send('Hello WeChat!')
    '''

    # 进入 Python 命令行、让程序保持运行
   
WidgetsDemo()