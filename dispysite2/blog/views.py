from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'blog bersama',
        'developer':'dada',
        'nav':[
            ['/','Home'],
            ['/blog/','Blog'],
            ['/blog/artikel/','artikel'],
            ['/blog/berita/','Berita'],
            ]
    } 
    return render(request,'blog/index.html',context)

