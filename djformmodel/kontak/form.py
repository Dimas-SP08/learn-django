from django import forms

class KontakForms(forms.Form):
    nama = forms.CharField(max_length=25)
    email = forms.EmailField()
    pesan = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'dada@gmail.com' in email:
            raise forms.ValidationError(f'ini dah {email} dipake')

        
        return email