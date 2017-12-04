from django.shortcuts import render


from django.http import HttpResponse




from django.db import connection

# Create your views here.

def home(request):
    # userName = request.GET["name"]
    # password = request.GET["password"]

    # (1552, 'wan', 'tou.jpg', '13587456984', '1234566', '13587456984',
    #  '68.45', '98.54', '987654', 'red_back0012', '125', '456', 'fs', '8552', 
    #  '88152584819494', '45', 'beijing', datetime.datetime(2017, 12, 4, 21, 25, 27))

    # cursor = connection.cursor()
    # cursor.execute("SELECT userid FROM user")
    # a = []
    # for row in cursor.fetchall():
    #     b = {"userid":row[0]}
    #     a.append(b)
 
    # print(a)
    userName = "1552"
    password = "wan"

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user WHERE userid=\"%s\" AND usename=\"%s\"'%(userName , password))
    a = cursor.fetchall()
    # print(a)

    if a:
        print("aaaaaaaaaaaaaaaaaaaaa")
        # successMSG = {"status":"ok","message":"登陆成功"}
        # return HttpResponse(json.dumps(successMSG) , content_type="application/json")
    else:
        pass
        print("bbbbbbbbbbbbbbbbbbbbbbb")
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
    cursor.execute('SELECT * FROM user WHERE userid=\"%s\" AND usename=\"%s\"'%(userName , password))
    a = cursor.fetchall()
    # print(a)
    if a:
        successMSG = {"status":"ok","message":"登陆成功"}
        return HttpResponse(json.dumps(successMSG) , content_type="application/json")
    else:
        errorMSG = {"status":"error","message":"登录失败"}
        return HttpResponse(json.dumps(errorMSG) , content_type="application/json")






    # cursor = connection.cursor()
    # selectName = cursor.execute('SELECT * FROM manager WHERE adminname=%s AND adminpassword=%s'%(userName , password))

    # if selectName:
    #     successMSG = {"status":"ok","message":"登陆成功"}
    #     return HttpResponse(json.dumps(successMSG) , content_type="application/json")

    # errorMSG = {"status":"error","message":"登录失败"}
    # return HttpResponse(json.dumps(errorMSG) , content_type="application/json")






