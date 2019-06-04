from .models import Classes
from django import forms


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Classes
        # widgets = {'days': forms.CheckboxSelectMultiple}
        fields = '__all__'
