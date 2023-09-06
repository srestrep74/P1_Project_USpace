from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
