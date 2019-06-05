# accounts/urls.py
# Configures url path for signup page
# Version 1.0
# Authors: Emma Carton (following tutorial)
# Dependencies: django library, accounts/views.py
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]
