from django.contrib import admin
from .models import Classes
from .forms import ClassesForm


class ClassesAdmin(admin.ModelAdmin):
    form = ClassesForm


admin.site.register(Classes, ClassesAdmin)
