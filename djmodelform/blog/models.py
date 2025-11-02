from django.db import models
from django.core import validators
# Create your models here.
from django.db import models
from .validatiions import validate_tag,validate_penulis
# Create your models here.


class Artikel(models.Model):
    judul = models.CharField(
        max_length=100,
        validators=[validators.MaxLengthValidator(6)])
    isi = models.TextField()
    DFT_KATEGORI = (
        ('berita', 'Berita'),
        ('blog', 'Blog'),
        ('jurnal', 'Jurnal'),
    )
    kategori = models.CharField(
        max_length=20,
        choices=DFT_KATEGORI,
        default='blog',
    )
    penulis = models.CharField(
        max_length=25,
        validators=[validate_penulis]
        )
    tag = models.CharField(max_length=25,
                           validators=[validate_tag])
    penerbit = models.CharField(max_length=50)


    def __str__(self):
        return "{} {}".format(self.id, self.judul)