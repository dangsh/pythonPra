from .models import *
from django.http import HttpResponse

def test(request):
    People.objects.create(name="ddd")
    return HttpResponse("qqqqqqqqqqq")