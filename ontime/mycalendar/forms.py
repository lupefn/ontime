from .models import Classes
from django import forms

class ClassesForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = '__all__'