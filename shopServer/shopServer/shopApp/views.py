from django.shortcuts import render


from django.http import HttpResponse




from django.db import connection

# Create your views here.

def home(request):
    # userName = request.GET["name"]
    # password = request.GET["password"]

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user")
    a = []
    for row in cursor.fetchall():
        b = {"userid":row}
        a.append(b)
 
    print(a)


    # if selectName:
    #     successMSG = {"status":"ok","message":"登陆成功"}
    #     return HttpResponse(json.dumps(successMSG) , content_type="application/json")

    # errorMSG = {"status":"error","message":"登录失败"}
    # return HttpResponse(json.dumps(errorMSG) , content_type="application/json")



    


    # cursor = connection.cursor()

    # cursor.execute('select * from manage')


    # cursor.execute('CREATE TABLE Persons(Id_P int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255))')

  
    # cursor.execute('create table xxx');


    # return render(request , "home.html");\
    return render(request , "home.html");


def error(request):
    return HttpResponse("我是404");



def goodsManage(request):
    return render(request , "goodsManage.html");


def userManage(request):
    return render(request , "userManage.html");

def orderManage(request):
    return render(request , "orderManage.html");

def adManage(request):
    return render(request , "adManage.html");

def activeManage(request):
    return render(request , "activeManage.html");


def loginApi(request):
 
    userName = request.GET["name"]
    password = request.GET["password"]

    cursor = connection.cursor()
    selectName = cursor.execute('SELECT * FROM manager WHERE adminname=%s AND adminpassword=%s'%(userName , password))

    if selectName:
        successMSG = {"status":"ok","message":"登陆成功"}
        return HttpResponse(json.dumps(successMSG) , content_type="application/json")

    errorMSG = {"status":"error","message":"登录失败"}
    return HttpResponse(json.dumps(errorMSG) , content_type="application/json")






