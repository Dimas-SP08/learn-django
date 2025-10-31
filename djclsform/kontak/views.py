from django.shortcuts import render
from .forms import KontakForm
# Create your views here.



def index(request):
    kontakForm = KontakForm()
    context = {
        'Judul': 'Kontak',
        'Heading': 'Kontak Forms',
        'kontak_form': kontakForm
    
    }

    if request.method == 'POST':
        context['nama'] =request.POST['nama']
        context['email'] =request.POST['email']
        context['pesan'] =request.POST['pesan']
        context['subjek'] =request.POST['subjek']
    return render(request,'kontak/index.html',context)