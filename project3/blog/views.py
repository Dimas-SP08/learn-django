from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'blog',
        'subtitle':'ini adlaah halaman blog',
        'banner':'blog/images/blog.png',
        'css_apps':'blog/css/css_blog.css'
    }
    return render(request,'blog/index.html',context)
