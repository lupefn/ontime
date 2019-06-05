# mycalendar/urls.py
# Configures url path for class add and class list pages
# Version 2.0
# Authors: Emma Carton
# Dependencies: django library, mycalendar/views.py
from django.urls import path
from . import views

urlpatterns = [
    path('classadd/', views.classadd, name='classadd'),
    path('classlist/', views.classes_from_db, name='classview'),
]

