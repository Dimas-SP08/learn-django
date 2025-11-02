from django.shortcuts import render
from . form import KontakForms
from .models import kontakModel as kontak
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    #! queryset ORM
    contacts = kontak.objects.all().order_by('-waktu_kirim')
    
    context = {
        'Judul': 'Kontak',
        'Heading': 'Daftar Kontak Masuk',
        'contacts':contacts
    }
    return render(request, 'kontak/index.html', context)


def create(request):
    kontak_f = KontakForms(request.POST or None)
    salah = None
    
    if request.method == 'POST':
        if kontak_f.is_valid():
        
            kontak.objects.create(
                nama = kontak_f.cleaned_data.get('nama'),
                email = kontak_f.cleaned_data.get('email'),
                pesan = kontak_f.cleaned_data.get('pesan'),
            )
            return HttpResponseRedirect("/kontak/")
        
        else:
            salah = kontak_f.errors

    context = {
        'Judul':'Kiim pesan',
        'Heading':'Kirim pesan',
        'kontak_f':kontak_f,
        'salah':salah
    }
    return render(request,'kontak/create.html',context)