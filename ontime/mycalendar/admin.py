# mycalendar/admin.py
# Configures how class information is displayed on the admin page
# Version 1.2
# Authors: Lupe Fernandez-Nunez, Emma Carton
# Dependencies: django.apps library, mycalendar/models.py, mycalendar/forms.py
from django.contrib import admin
from .models import Classes, DaysOfTheWeek
from .forms import CoursesForm


class ClassesAdmin(admin.ModelAdmin):
    form = CoursesForm
    list_display = ['CRN', 'for_user', 'name', 'credits', 'professor', 'location', 'start_time', 'end_time',
                    'start_date',
                    'end_date']
    list_filter = ['name', 'credits', 'professor', 'start_time', 'end_time']
    fields = ['CRN', 'for_user', 'name', 'credits', 'professor', 'location', ('start_time', 'end_time'), ('start_date', 'end_date'),
              'frequency_of_course']




admin.site.register(Classes, ClassesAdmin)
