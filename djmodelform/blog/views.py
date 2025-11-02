from django.shortcuts import render,redirect
from .forms import ArtikelForm
from .models import Artikel


# Create your views here.
def index(request):
    articles = Artikel.objects.all()

    context = {
        'Judul': ' Blog',
        'Heading': 'Halaman daftar Artikel Blog',
        'articles':articles
       
    }
    return render(request,'blog/index.html',context)

def create_artikel(request):
    
    if request.method == 'POST':
        form = ArtikelForm(request.POST or None)
        if form.is_valid():
            
            form.save()
            return redirect('blog:index')
        
    else:
        form = ArtikelForm()

    context = {
        'Judul': ' Artikel',
        'Heading': 'Buat Artikel',
        'form':form,
    }

    return render(request,'blog/create.html',context)