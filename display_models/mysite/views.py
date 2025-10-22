from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title':'diajar',
        'subtitle':'bersam sama'
    }
    return render(request,'index.html',context)

