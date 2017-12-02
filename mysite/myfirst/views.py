from django.shortcuts import render
from django.http import HttpResponse
from myfirst.models import MyStudent
import json
# Create your views here.

def hello(request):
    return HttpResponse("<h1>我是hello界面</h1>")
def error(request):
    return HttpResponse("<h1>我是error界面</h1>")
def home(request):
    return render(request , "home.html")
def parse(request , aaa):
    return HttpResponse("<h1>我是parse界面....%s</h1>"%aaa)

#home 界面数据接口
def getHomeData(request):
    myArr = []
    arr = MyStudent.objects.all()
    for item in arr:
        name = item.name
        age = item.age
        tempDic = {"name":name , "age":age}
        myArr.append(tempDic)
    return HttpResponse(json.dumps(myArr) , content_type="application/json")


def deleteOne(request):
    print("正在删除。。。。。。。。" , request.GET["name"])
    deleteName = request.GET["name"]
    
    c = MyStudent.objects.get(name=deleteName)
    # c = MyStudent.objects.all()
    c.delete()
    statusDic = {"message":"ok"}
    return HttpResponse(json.dumps(statusDic) , content_type="application/json")

def updateOne(request):
    # name = request.GET["name"]
    # newAge = request.GET["newAge"]
    # print("(((((((((((((((((((((" + name , newAge)
    # c = MyStudent.objects.get(name=name)
    # c.age = newAge
    # c.save()
    # return HttpResponse("修改成功")
    pass

# # 添加一个联系人
# def addOne(request):
#     name = request.GET["name"]
#     age = request.GET["age"]
#     MyStudent.objects.create(name=name , age=age)
#     return HttpResponse("添加成功")

def addOne(request):
    getName = request.GET["name"] #获取名字
    getAge = request.GET["age"]    #获取年龄


    dictArr = []        #创建字典数组
    arr = MyStudent.objects.all()  #遍历数据库中的数据
    for item in arr:    #获取每一个对象  将其添加到字典数组中
        name1 = item.name    
        age1 = item.age
        dictArr.append({"name":name1 , "age":age1})
    
    print(dictArr)

    for i in dictArr:
        if i["name"] == getName:
            c = MyStudent.objects.get(name=i["name"])
            c.age = getAge
            c.save()

            return HttpResponse("更新成功")
        else:
            pass
    MyStudent.objects.create(name=getName , age=getAge)
    return HttpResponse("添加成功")