
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class ChangePasswordUserForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','new_password','new_password2']