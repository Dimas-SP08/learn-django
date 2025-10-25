from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>halaman beranda</h1>")
def detail_ar(request,kategori):
    at = kategori
    headline = "<h1>halaman nomor arsip</h1>"
    return HttpResponse(headline+at)
def arsip(request,input):
    headline = "<h1>halaman nomor arsip</h1>"
    no_arsip = input
    return HttpResponse(f'headline {no_arsip}')



def tahun_arsip(request,tahun):
    at = tahun
    headline = "<h1>halaman nomor arsip</h1>"
    return HttpResponse(headline+at)




# def tgl_arsip(request,tgl,bln,thn):
#     headline = "<h1>penanggalan nomor arsip</h1>"
#     no_arsip = tgl
#     bulan = bln
#     tahun = thn
#     return HttpResponse(f'headline {no_arsip} {bulan} {tahun}')


def tgl_arsip(request,**input):
    headline = "<h1>penanggalan nomor arsip</h1>"
    no_arsip = input['tgl']
    bulan =    input['bln']
    tahun =    input['thn']
    return HttpResponse(f'<h3> {headline} {no_arsip} {bulan} {tahun}</h3>')




