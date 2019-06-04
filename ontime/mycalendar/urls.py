from django.urls import path
from . import views

urlpatterns = [
    path('classadd/', views.classadd, name='classadd'),
    path('classlist/', views.classes_from_db, name='classview'),
]

