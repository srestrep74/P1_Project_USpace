from django import forms
from .models import *

class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]


class reminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ["space_id", "remember_to", "user_id"]