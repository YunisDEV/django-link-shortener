from django import forms
from django.contrib.auth.models import User
from django.forms import fields

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]