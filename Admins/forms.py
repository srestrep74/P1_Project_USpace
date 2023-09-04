from django import forms
from .models import *


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ('name', 'description', 'availability', 'classification')