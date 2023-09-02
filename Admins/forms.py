from django import forms
from .models import *


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = '__all__'