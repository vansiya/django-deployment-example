from django import forms
from appLogin.models import UserProFilesInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields =('username','password','email')

class UserProFileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProFilesInfo
        fields = ('portfolio_site','profile_pic')