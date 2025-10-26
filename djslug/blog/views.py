from django.shortcuts import render
from .models import Artikel
# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'blog', 'headline': 'selamat datang di halaman blog'})

def kategori(request,kategoriInput):
    category = Artikel.objects.filter(kategori=kategoriInput)
    context = {
        'title':'kategori',
        'headline':'artikel kategori',
        'categories':category
    }
    return render(request,'kategori.html',context)


def detail_artikel(request,slugInput):
    articles = Artikel.objects.get(slug=slugInput)
    context = {
        'title':'detail_artikel',
        'headline':' detail _artikel',
        'articles':articles

    }
    return render (request,'detail_artikel.html',context)