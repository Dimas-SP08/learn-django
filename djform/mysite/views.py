from django.shortcuts import render

def index(request):
    context = {
        'Judul':'Home',
        'Heading':'django forms',
    }

    if request.method == 'POST':
        context['nama'] =request.POST['nama']
        context['email'] =request.POST['email']
        print('ini post')

    else:
        print('ini get punya')
    return render(request, 'index.html',context)