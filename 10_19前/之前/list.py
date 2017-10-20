
#C:\Users\张霄港\Desktop\python
from tkinter import *
from wxpy import *
class WidgetsDemo:
   
    # 初始化机器人，扫码登陆
    bot = Bot(cache_path=True);
    def __init__(self):
        master=Tk()
        master.title("微信聊天")
        '''
        listbox=Listbox(master)#创建一个列表
        for i in range(20):
            listbox.insert(END,str(i))
        '''
        self.name=StringVar()
        self.name2=StringVar()
        labal1=Label(master, text="名称")
        labal2=Label(master, text="信息")
        e1=Entry(master,textvariable=self.name)
        e2=Entry(master,textvariable=self.name2)
        sendBtn=Button(master,text="搜索姓名",command=self.searchFn)
        sendBtn2=Button(master,text="发送信息",command=self.sendFn)
        
        labal1.grid(row=0,column=1)#名称
        labal2.grid(row=1,column=1)#信息
        e1.grid(row=0,column=2)#名称栏
        e2.grid(row=1,column=2)#信息栏
        sendBtn.grid(row=0,column=3)#获取名称按钮
        sendBtn2.grid(row=1,column=3)#发送信息按钮
        
        mainloop()

    
    def searchFn(self):
        self.toUser=self.bot.friends().search(self.name.get())[0];
    def sendFn(self):
        sendMsg=self.name2.get();
        self.toUser.send(sendMsg);

   # 进入 Python 命令行、让程序保持运行
    embed()

WidgetsDemo()
