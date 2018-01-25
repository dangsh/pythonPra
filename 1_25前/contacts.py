from tkinter import *
import shelve

root = Tk();
root.title("通讯录");

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

db = shelve.open("contacts");
getDataFromDbToArr(db , MyContacts.arr);

phoneList = Listbox(root);
phoneList.pack();
for val in MyContacts.arr:
    phoneList.insert(END , val.name);

nameLabel = Label(root , text="姓名");
nameLabel.pack();

nameEntry = Entry(root);
nameEntry.pack();

phoneLabel = Label(root , text="电话号码");
phoneLabel.pack();



phoneEntry = Entry(root);
phoneEntry.pack();

nameEntry.bind("<FocusIn>" , nameFocusIn);
nameEntry.bind("<FocusOut>" , nameFocusOut);
phoneEntry.bind("<FocusIn>" , phoneFocusIn);
phoneEntry.bind("<FocusOut>" , phoneFocusOut);


addBtn = Button(root , text="添加" , command=addBtnFn);
addBtn.pack();
addBtn.config(state=DISABLED);

showBtn = Button(root , text="显示" , command=showBtnFn);
showBtn.pack();

deleteBtn = Button(root , text="删除" , command=deleteBtnFn);
deleteBtn.pack();

# 回车事件
def returnFn(event):
    addBtnFn();

# 给整个窗口添加点击事件
root.bind("<Return>" , returnFn);

root.mainloop();



