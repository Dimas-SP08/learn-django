from django import forms
from .models import Artikel
# class ArtikelForm(forms.Form):
#     judul = forms.CharField( max_length=100, required=False)
#     isi = forms.CharField(widget=forms.Textarea())
#     kategori = forms.CharField( max_length=20, required=False)

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = '__all__' #['penulis','judul','isi','kategori','tag','penerbit']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['judul'].widget.attrs.update({'class':'form-control','placeholder':'masukkan Judul artikel'})
        self.fields['isi'].widget.attrs.update({'class':'form-control','placeholder':'masukkan Judul artikel'})
        self.fields['kategori'].widget.attrs.update({'class':'form-select','placeholder':'masukkan Judul artikel'})
        self.fields['penulis'].widget.attrs.update({'class':'form-control','placeholder':'masukkan Judul artikel'})
        self.fields['penerbit'].widget.attrs.update({'class':'form-control','placeholder':'masukkan Judul artikel'})
        self.fields['tag'].widget.attrs.update({'class':'form-control','placeholder':'masukkan Judul artikel'})

















