from django import forms
from .models import *

class comment_form(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["comment"]