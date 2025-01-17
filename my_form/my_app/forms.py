from django import forms
from my_app.models import UserProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio','picture')
