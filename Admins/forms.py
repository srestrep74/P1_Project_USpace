from django import forms
from .models import *


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ('name', 'description', 'availability', 'classification', 'longitude', 'latitude', 'image')
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }
        labels = {
            'image': 'Imagen del espacio',
        }
        help_texts = {
            'image': 'Seleccione una imagen para el espacio.',
        }
        error_messages = {
            'image': {
                'invalid': "El archivo debe ser una imagen.",
            },
        }