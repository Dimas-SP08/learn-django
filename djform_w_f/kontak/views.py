from django.shortcuts import render
# Create your views here.
from .forms import KontakForms



def index(request):
    formfield = KontakForms()

    context = {
        'Judul': 'Kontak',
        'Heading': 'Kontak Forms',
        'kontak_forms':formfield
        
    
    }
    
    return render(request,'kontak/index.html',context)