from django.shortcuts import render
from .models import Artikel
def index(request):
    articles = Artikel.objects.all()
    context = {
        'judul':'Blog',
        'heading':'Hal blog',
        'Artikel': articles,
    }
    return render(request,'blog/index.html',context)


def detail_artikel(request, slugInput):
    detail_articles = Artikel.objects.get(slug_art=slugInput)
    context = {
        'Judul': 'Detail Blog',
        'Heading': 'Halaman Detail Blog',
        'DetailArtikel': detail_articles,
    }
   
    return render(request, 'blog/detail.html', context)