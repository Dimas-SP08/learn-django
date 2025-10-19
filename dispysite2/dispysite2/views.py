from django.shortcuts import render

# Create your views here.
def index(request):
    contex = {
        'title':'web development',
        'developer':'diespy'
    }
    return render(request,'index.html',contex)