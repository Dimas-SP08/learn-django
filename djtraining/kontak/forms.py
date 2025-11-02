from django import forms
class KontakForms(forms.Form):
    name = forms.CharField(
        label='Nama Lengkap',
        max_length=25,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'masukkan nama lenkap anda'            }
        )
    )
    email = forms.EmailField(
        help_text='masukkan email anda dengan benar'
    )
    jenkel = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'class':'form-check-input'
            }
        ),
        label='Jenis Kelamin',
        choices=[
        ('p','pria'),
        ('w','wanita'),
    ],
    )
    tgl_lahir = forms.DateField(
        label='Tanggal Lahir',
        widget=forms.SelectDateWidget(
            years=range(1988,2025,1),
            attrs={
                'class':'form-select'
            })
        )
    pesan = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'masukkan pesan anda'
        }
    ))
    agree = forms.BooleanField()

    email.widget.attrs.update({'class':'form-control','placeholder':'masukkan email anda'
})