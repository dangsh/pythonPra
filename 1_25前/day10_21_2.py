from tkinter import *
from xpinyin import Pinyin
import shelve

root = Tk()
root.title("phone book")
root.geometry('600x400')
l = Label(root , text = '---PHONE BOOK---' , bg = 'green' , font = ("Arial" , 12) , width = 600 , height = 2)
l.pack()
# root.resizable(width = True , height = True)

frm = Frame(root)

class MyContacts:
    arr = [];

class MyPhone:
    def __init__(self , name , phone):
        self.name = name;
        self.phone = phone;

    def __str__(self):
        return "[name=%s , phone=%s]  " % (self.name , self.phone);


# 将数据放进数据库中
def addDataToDb(tempData):
    db[tempData.name] = tempData;

# 将数据库中的数据取出来
# 放到界面数据源 MyContacts.arr中
def getDataFromDbToArr(db , arr):
    for key in db:
        tempObj = db[key];
        arr.append(tempObj);

# 打印数组中的每一个元素
def printArray(arr):
    for item in arr:
        print(item);

# 显示数据的方法
def showBtnFn():
    printArray(MyContacts.arr);



def addBtnFn():
    name = nameEntry.get();
    phone = phoneEntry.get();
    tempObj = MyPhone(name , phone);
    isHaveThisName = False;
     
    for item in MyContacts.arr:
        if item.name == name:
            isHaveThisName = True;
            break;

    if isHaveThisName:
        for item in MyContacts.arr:
            if item.name == name:
                item.phone = phone;

        
    else: 
        # 添加新元素
        MyContacts.arr.append(tempObj);
        phoneList.insert(END , tempObj.name);

    addDataToDb(tempObj);
    var_name.set("");
    var_phone.set("")
    
# 删除
def deleteBtnFn():
    selects = phoneList.curselection();
    selectIndex = selects[0];
    phoneList.delete(selectIndex);

    # 根据下标从数据源中删除
    phoneObj = MyContacts.arr[selectIndex];
    MyContacts.arr.remove(phoneObj);

    # 根据下标从数据库中删除
    phoneName = phoneObj.name;
    del db[phoneName];


# 输入框的检测方法
def nameFocusIn(event):
    print("name 输入框 获得焦点");
def nameFocusOut(event):
    if len(nameEntry.get()) > 0:
        addBtn.config(state=NORMAL);
def phoneFocusIn(event):
    print("phone 输入框 获得焦点");
def phoneFocusOut(event):
    print("phone 输入框 失去焦点");

# 回车事件
def returnFn(event):
    addBtnFn();

def showMessage():
    selects = phoneList.curselection();
    selectIndex = selects[0];
    phoneObj = MyContacts.arr[selectIndex];
    a = "name: %s  , phone: %s" %(phoneObj.name , phoneObj.phone)
    var_message.set(a)

#****************************************
#***********以上是类，方法的定义***********
#****************************************

db = shelve.open("contacts");
getDataFromDbToArr(db , MyContacts.arr);

#******************左边*******************
frm_L = Frame(frm)
Label(frm_L , text = '电话簿内容|' , font = ('Arial' , 15)).pack(side = TOP)
frm_L.pack(side = LEFT)
#*****************************************
phoneList = Listbox(frm_L);
phoneList.pack();
for val in MyContacts.arr:
    phoneList.insert(END , val.name);


var_message = StringVar()
phoneEntry = Entry(frm_L , textvariable = var_message);
phoneEntry.pack();

#******************右边*******************
frm_R = Frame(frm)
Label(frm_R , text = '|电话簿功能' , font = ('Arial' , 15)).pack(side = TOP)
frm_R.pack(side = RIGHT)
#*****************************************


nameLabel = Label(frm_R , text="姓名");
nameLabel.pack();


var_name = StringVar()
nameEntry = Entry(frm_R , textvariable = var_name);
nameEntry.pack();

phoneLabel = Label(frm_R , text="电话号码");
phoneLabel.pack();


var_phone = StringVar()
phoneEntry = Entry(frm_R , textvariable = var_phone);
phoneEntry.pack();

nameEntry.bind("<FocusIn>" , nameFocusIn);
nameEntry.bind("<FocusOut>" , nameFocusOut);
phoneEntry.bind("<FocusIn>" , phoneFocusIn);
phoneEntry.bind("<FocusOut>" , phoneFocusOut);


addBtn = Button(frm_R , text="添加" , command=addBtnFn);
addBtn.pack();
addBtn.config(state=DISABLED);

showBtn = Button(frm_R , text="显示" , command=showBtnFn);
showBtn.pack();

showMessageBtn = Button(frm_R , text="显示信息" , command=showMessage);
showMessageBtn.pack();

deleteBtn = Button(frm_R , text="删除" , command=deleteBtnFn);
deleteBtn.pack();


# root.bind("<Return>" , returnFn);


frm.pack()
root.mainloop()