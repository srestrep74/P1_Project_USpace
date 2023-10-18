from django import forms
from .models import *


class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ["remember_to"]


class DamageForm(forms.ModelForm):
    class Meta:
        model = Damage
        fields = ["space_name", "description", "image"]