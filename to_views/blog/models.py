from django.db import models

class Kategori(models.Model):
    kode = models.CharField(max_length=7)
    nama = models.CharField(max_length=255)
    def __str__(self):
        return "%d. %s" % (self.id, self.nama)


# Create your models here.
class Article(models.Model):
    judul = models.CharField(max_length=250)
    isi = models.TextField(null=True)
    PILIHAN_KATEGORI= [
        ('python','python'),
        ('django','django'),
        ('javascript','javascript'),
    ]
    categories = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    tanggalPublik = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%d. %s" % (self.id, self.judul)
    

