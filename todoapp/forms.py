from django import forms
from django.forms import ModelForm

from .models import *

class todoappform(forms.ModelForm):
    
    
    class Meta:
        model=todo
        fields='__all__'
