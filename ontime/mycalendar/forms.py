# mycalendar/forms.py
# Configures form to get class information on classadd page
# Version 1.3
# Authors: Emma Carton
# Dependencies: django.apps library, mycalendar/models.py
from .models import Classes
from django import forms


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = '__all__'
