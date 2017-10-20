from tkinter import *
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(cache_path=True);
root = Tk() 
listbox = Listbox(root) 
listbox.pack()

listData=bot.friends(update=False);

 
a=[]


for i in range(len(listData)):
    #print(i,listData[i])
    a.append(listData[i])

#现在数据都在list a 里


for i in range(len(a)):
    b=listData[i]
    listbox.insert(END,str(b))

mainloop()



# 进入 Python 命令行、让程序保持运行
#embed()

