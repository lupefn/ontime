from django.urls import path

from . import views


urlpatterns = [
    path('classadd/', views.index, name='classadd'),
]