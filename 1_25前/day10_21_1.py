#tkinter
from tkinter import *
from xpinyin import Pinyin
import shelve
class Phone:
    def __init__(self , name , number):
        self.name = name
        self.number = number

    def __str__(self):
        return "name: %s , number: %s" %(self.name , self.number)


def addNum():
    n = var.get()
    m = var1.get()
    p = Phone(n , m)

    
    # list_item.append("name: %s , number: %s" %(n , m))

    db = shelve.open("shujuku")
    db[n] = p
    print(db[n])
    db.close();
    # print('姓名是：%s , 电话号是：%s '% (var.get() , var1.get()))
    

root = Tk()
root.title("phone book")
root.geometry('600x400')
l = Label(root , text = '---PHONE BOOK---' , bg = 'green' , font = ("Arial" , 12) , width = 600 , height = 2)
l.pack()
# root.resizable(width = True , height = True)
frm = Frame(root)

#******************左边*******************
frm_L = Frame(frm)
Label(frm_L , text = '电话簿内容|' , font = ('Arial' , 15)).pack(side = TOP)
frm_L.pack(side = LEFT)
#*****************************************



var_list = StringVar()
lb = Listbox(frm_L , listvariable = var_list)

list_item =[]
db = shelve.open("shujuku")
for i in db:
    p = db[i]
    list_item.append("name: %s , number: %s" %(p.name , p.number))
db.close()

# var_list.set(a for a in list_item)

for item in list_item:
    lb.insert(END , item)


lb.pack()







#******************右边*******************
frm_R = Frame(frm)
Label(frm_R , text = '|电话簿功能' , font = ('Arial' , 15)).pack(side = TOP)
frm_R.pack(side = RIGHT)
#*****************************************

r1 = Label(frm_R , text = '添加' , bg = 'green' , font = ("Arial" , 12) )
r1.pack()

r2 = Label(frm_R , text = '姓名：' , font = ("Arial" , 12) )
r2.pack()
var = StringVar()
e = Entry(frm_R , textvariable = var)
e.pack()

r3 = Label(frm_R , text = '手机号：' , font = ("Arial" , 12) )
r3.pack()
var1 = StringVar()
e1 = Entry(frm_R , textvariable = var1)
e1.pack()


Button(frm_R , text = '提交' , command = addNum).pack()




frm.pack()
root.mainloop()