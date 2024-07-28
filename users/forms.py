from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=255, label="username", widget=forms.TextInput(attrs={"class" : "username_input"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "password_input"}))
    

class RegisterUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
