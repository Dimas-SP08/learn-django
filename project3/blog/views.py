from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'blog',
        'subtitle':'ini adlaah halaman blog',
    }
    return render(request,'blog/index.html',context)
