from django.shortcuts import render

def index(request):
    context = {
        'judul':'Home',
        'heading':'welcome'
    }
    return render(request,'index.html',context)