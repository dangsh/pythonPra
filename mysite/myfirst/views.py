from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("我是hello界面")


def home(request):
    return HttpResponse("<h1>我是home界面</h1>")