# phone book 类
# 增删改查 
# 电话对象phone 类：  姓名 电话号码
from xpinyin import Pinyin
        
class Phone:
    def __init__(self , name , number):
        self.name = name
        self.number = number
    
    # def tall(self):
    #     print('我的名字是',self.name)
    #     print('******************')

def addNum():
    n = input('请输入要添加的姓名:::')
    m = input('请输入他的电话号:::')
    p = Phone(n , m)
    # p.tall()
    pb.append(p)
    # for i in pb:
    #     print(i.name , i.number)
    
        
def delete():
    
    n = input('请输入要删除的姓名:::')
    for i in pb:
        if i.name == n:
            pb.remove(i)
def change():
    n = input('请输入要修改电话号的姓名:::')
    m = input('请输入要修改成的手机号:::')
    for i in pb:
        if i.name == n:
            i.number = m
            
def find():
    n = input('请输入要查找电话号的姓名:::')
    for i in pb:
        if i.name == n:
            print('他的电话号是:::',i.number)

def listNum():
    print('******************')
    
    for i in pb:
        print('姓名:%s , 电话号:%s' % (i.name , i.number))
    print('******************')

def sortBook():
    
    x = Pinyin()
    for i in pb:
        a = x.get_pinyin(i.name)
        print(a)

    


pb = []
while True:
    print('******************')
    print('可以选择的功能如下：')
    print('1.添加')
    print('2.删除')
    print('3.修改')
    print('4.查找')
    print('5.排序')
    print('6.列举电话本中的内容')


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
    else:
        print('******************')
        print('*不要输入其他内容！*')
        