from django.shortcuts import render

# Create your views here.
from django import forms

class KontakForm(forms.Form):
    nama = forms.CharField()


def index(request):
    kontakForm = KontakForm()
    context = {
        'Judul': 'Kontak',
        'Heading': 'Kontak Forms',
        'kontak_form': kontakForm
    
    }

    return render(request,'kontak/index.html',context)