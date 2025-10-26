from django.shortcuts import render
from .models import Artikel
def index(request):
    articles = Artikel.objects.all()
    category = Artikel.objects.values('kategori__nama').distinct() # distinct biar ngilangin data yang sama  jadi 1

    context = {
        'judul':'Blog',
        'heading':'Hal blog',
        'Artikel': articles,
        'Categories': category,
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



def kategori_artikel(request, kategoriInput):
    articles = Artikel.objects.filter(kategori__nama=kategoriInput)
    category = Artikel.objects.values('kategori__nama').distinct() # distinct biar ngilangin data yang sama  jadi 1
    
    context = {
        'Judul': 'kategori Blog',
        'Heading': 'Halaman berdasarkan kategori Blog',
        'Articles': articles,
        'Categories': category,
    }
    return render(request, 'blog/kategori.html', context)