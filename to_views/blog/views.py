from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    semuaartikel = Article.objects.order_by('-judul')
    print(semuaartikel)
    context = {
        'title':'blog',
        'headline':'selamat datang di halaan blog',
        'articles':semuaartikel
    }
    return render(request,'index.html',context)

def blog(request):
    semuaartikel = Article.objects.filter(categories__nama = 'berita')
    print(semuaartikel)
    context = {
        'title':'blog',
        'headline':'selamat datang di halaan blog',
        'articles':semuaartikel
    }
    return render(request,'index.html',context)

def asd(request):
    semuaartikel = Article.objects.exclude(categories__nama= 'berita')
    print(semuaartikel)
    context = {
        'title':'blog',
        'headline':'selamat datang di halaan blog asd',
        'articles':semuaartikel
    }
    return render(request,'index.html',context)

def dasd(request):
    semuaartikel = Article.objects.filter(categories__nama = 'dasd')
    print(semuaartikel)
    context = {
        'title':'blog',
        'headline':'selamat datang di halaan blog dasd',
        'articles':semuaartikel
    }
    return render(request,'index.html',context)