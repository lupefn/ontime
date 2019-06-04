from django.contrib import admin
from .models import Classes, DaysOfTheWeek
from .forms import CoursesForm


class ClassesAdmin(admin.ModelAdmin):
    form = CoursesForm
    list_display = ['CRN', 'name', 'credits', 'professor', 'location', 'start_time', 'end_time', 'start_date',
                    'end_date']
    list_filter = ['name', 'credits', 'professor', 'start_time', 'end_time']
    fields = ['CRN', 'name', 'credits', 'professor', 'location', ('start_time', 'end_time'), ('start_date', 'end_date'), 'frequency_of_course']


class WeekdaysAdmin(admin.ModelAdmin):
    model = DaysOfTheWeek


admin.site.register(Classes, ClassesAdmin)
admin.site.register(DaysOfTheWeek, WeekdaysAdmin)
