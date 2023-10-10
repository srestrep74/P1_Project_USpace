from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import user_m
from django.forms import EmailField


class user_form(UserCreationForm):
    class Meta :
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class user_update_form(forms.ModelForm):
    class Meta:
        model = user_m
        fields = '__all__'
        exclude = ['user']

