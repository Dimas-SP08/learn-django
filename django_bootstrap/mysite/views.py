from django.shortcuts import render

def index(request):
    context = {
        'title':'portofolio',
        'subtitle':'welcome to my portofolio',
        'banner':'/images/home.png'
    }
    return render(request,'index.html',context)