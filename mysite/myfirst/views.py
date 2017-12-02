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
    myArr = []
    # return HttpResponse("<h1>我是home界面</h1>")

    #插入10条数据
    # for i in range(10):
    #     MyStudent.objects.create(name = "名字" + str(i))


    datas = MyStudent.objects.all()
    # return render(request , "home.html" , {"data" : datas})
    
    # myDic = {"name":"zhangsan" , "age":13}
    # return HttpResponse(json.dumps(myDic) , content_type="application/json")

    #将数据传递给界面模板 和 js标签中
    for data in datas:
        temp = {"name":data.name , "age":data.age}
        myArr.append(temp)
    
    
    return render(request , "home.html" , {"allStudents" : json.dumps(myArr)})



def parse(request , aaa):

    return HttpResponse("<h1>我是parse界面....%s</h1>"%aaa)