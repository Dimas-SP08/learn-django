from django.shortcuts import render

def index(request):
    context = {
        'title':'portofolio',
        'subtitle':'welcome to my portofolio',
        'banner':'/images/home.png'
    }
    return render(request,'index.html',context)

def login(request):
    context = {
        'title':'login',
        
    }
    return render(request,'login.html',context)
def daftar(request):
    context = {
        'title':'daftar',
        
    }
    return render(request,'daftar.html',context)