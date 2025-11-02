from django.shortcuts import render

def index(request):
    context = {
        'Judul':'Beranda',
        'Heading':'selamat datang'
    }
    return render(request,'index.html',context)