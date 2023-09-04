from django import forms
from .models import *


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
<<<<<<< HEAD
        fields = ('name', 'description', 'availability', 'classification')
=======
        fields = '__all__'
>>>>>>> sebas
