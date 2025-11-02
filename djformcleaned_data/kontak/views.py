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
    kontak_f = KontakForms()
    if request.method == 'POST':
        print(request.POST)
        kontak.objects.create(
            nama = request.POST.get('nama'),
            email = request.POST.get('email'),
            pesan = request.POST.get('pesan'),
        )
        return HttpResponseRedirect("/kontak/")

    context = {
        'Judul':'Kiim pesan',
        'Heading':'Kirim pesan',
        'kontak_f':kontak_f
    }
    return render(request,'kontak/create.html',context)