from django.shortcuts import render,redirect
from .models import Tujuan
from .forms import TujuanForm
# Create your views here.
def index(request):
    semua_tujuan = Tujuan.objects.all()
    context = {
        'Judul': 'Daftar Tujuan',
        'Heading': 'Daftar Tujuan',
        'semua_tujuan':semua_tujuan
    }
    return render(request, 'pulangpergi/index.html', context)

def add_tujuan(request):

    if request.method == 'POST':
        form = TujuanForm(request.POST or None)
        if form.is_valid():
            form.save()

            return redirect('pulangpergi:index')
        
    else:
        form = TujuanForm()

    context = {
        'Judul': 'Tambah daftar tujuan',
        'Heading': 'Tambah daftar tujuan',
        'form':form,
    }
    return render(request,'pulangpergi/create.html',context)


def delete(request,nm_slug):
    Tujuan.objects.filter(slug=nm_slug).delete()
    return redirect('pulangpergi:index')