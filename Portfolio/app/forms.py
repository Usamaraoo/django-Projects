from django import forms
from .models import *


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'
