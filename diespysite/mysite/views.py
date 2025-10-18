from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def blog(request):
    return HttpResponse('<h1>ini adlaah hal blog</h1>')