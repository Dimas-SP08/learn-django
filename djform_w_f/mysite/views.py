from django.shortcuts import render
from .forms import FormField

def index(request):
    formfield = FormField()
    context = {
        'Judul':'field',
        'Heading':'django forms',
        'form_fields':formfield
    }
    return render(request, 'index.html',context)