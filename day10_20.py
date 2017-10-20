from xpinyin import Pinyin
import shelve
        
class Phone:
    def __init__(self , name , number):
        self.name = name
        self.number = number

    def __str__(self):
        return "name: %s , number: %s" %(self.name , self.number)
    

def addNum():
    n = input('请输入要添加的姓名:::')
    m = input('请输入他的电话号:::')
    p = Phone(n , m)
    db = shelve.open("shujuku")
    db[n] = p
    print(db[n])
    db.close();
      
def delete():
    
    n = input('请输入要删除的姓名:::')
    db = shelve.open("shujuku")
    del db[n]
    db.close()
            
def change():
    n = input('请输入要修改电话号的姓名:::')
    m = input('请输入要修改成的手机号:::')
    db = shelve.open("shujuku")
    p = db[n]
    p.number = m
    db[n] = p
    print(db[n])
    db.close()
    
            
def find():
    n = input('请输入要查找电话号的姓名:::')
    db = shelve.open("shujuku")
    p = db[n]
    print(db[n])
    db.close()

def listNum():
    print('******************')
    db = shelve.open("shujuku")
    for i in db:
        p = db[i]
        print(db[i])
    db.close()
    
    print('******************')

def sortBook():
    
    # x = Pinyin()
    # for i in pb:
    #     a = x.get_pinyin(i.name)
    #     print(a)
    pass
    

while True:
    print('******************')
    print('可以选择的功能如下：')
    print('1.添加')
    print('2.删除')
    print('3.修改')
    print('4.查找')
    print('5.排序')
    print('6.列举电话本中的内容')
    print('7.退出程序')


    a = input ('请选择功能：：：')
    if a == '1':
        addNum()
    elif a =='2':
        delete()
    elif a == '3':
        change()
    elif a == '4':
        find()
    elif a == '5':
        sortBook()
    elif a == '6':
        listNum()
    elif a == '7':
        quit()
    else:
        print('******************')
        print('*不要输入其他内容！*')
        