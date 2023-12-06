# from django.http import HttpResponse
from django.shortcuts import render

# def hello(request):
#     return HttpResponse('<h1>Hello Django !</h1>')


def page(request):
    
    return render(request, 'authenti/hello.html')

# def home(request):
    
#     return render(request, 'authenti/home.html')