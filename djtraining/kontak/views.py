from django.shortcuts import render
from .forms import KontakForms
# Create your views here.
def index(request):
    kontak_form = KontakForms()
    context = {
        'judul':'kontak',
        'heading':'kontak form',
        'f_kontak':kontak_form
    }
    print(request.POST)
    return render(request,'kontak/index.html',context)