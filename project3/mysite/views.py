from django.shortcuts import render

def index(request):
    context = {
        'title':'portofolio',
        'subtitle':'welcome to my portofolio',
        'nav': [
            ['/','Home'],
            ['/blog/','Blog'],
            ['/kontak/','Kontak']
        ]
    }
    return render(request,'index.html',context)