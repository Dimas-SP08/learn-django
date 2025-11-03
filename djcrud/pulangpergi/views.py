from django.shortcuts import render,redirect,get_object_or_404
from .models import Tujuan
from .forms import TujuanForm
from django.contrib import messages
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
        form = TujuanForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

            messages.success(request,'Data Berhasil di tambahkan')
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
    messages.info(request,'Data berhasil di hapus')
    return redirect('pulangpergi:index')

def update(request,nm_slug):    
    # obj_tujuan = Tujuan..get(slug=nm_slug)
    obj_tujuan = get_object_or_404(Tujuan, slug = nm_slug )

    if request.method == 'POST':
        form = TujuanForm(request.POST or None, request.FILES or None,instance= obj_tujuan)
        if form.is_valid():
            
            form.save()
            messages.warning(request,'berhasil di update')
            return redirect('pulangpergi:index')
        
    else:
        form=TujuanForm(instance=obj_tujuan)


    context = {
        'Judul': 'edit daftar tujuan',
        'Heading': 'edit daftar tujuan',
        'form':form,
    }
    return render(request,'pulangpergi/update.html',context)
