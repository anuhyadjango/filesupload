from django import forms
from .models import *
class resumeform(forms.ModelForm):
    class Meta:
        model = profiles
        fields = '__all__'