from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """
    index视图

    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """
    return HttpResponse("hello index")


def weather(request, city, year):
    print(city)
    print(year)
    return HttpResponse("ok")