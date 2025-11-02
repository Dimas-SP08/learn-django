from django import forms
from . models import Tujuan
class TujuanForm(forms.ModelForm):
    class Meta:
        model = Tujuan
        fields = "__all__"



    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['nm_penumpang']. widget.attrs.update({'class':'form-control','paceholeder':'masukkan nama penumpang anda!'})
        self.fields['nm_pengemudi']. widget.attrs.update({'class':'form-control','paceholeder':'masukkan nama pengemudi anda!'})
        self.fields['tujuan']. widget.attrs.update({'class':'form-control','paceholeder':'masukkan Tujuan anda!'})
    