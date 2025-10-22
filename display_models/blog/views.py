from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.
def index(request):
    #query set
    allartikel = Article.objects.all()
    context = {
        'title':'diajar',
        'subtitle':'bersam sama',
        'semuaartikel':allartikel,
    }
    return render(request,'index.html',context)

