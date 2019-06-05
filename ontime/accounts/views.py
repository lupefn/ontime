# accounts/views.py
# Defines what will be displayed on signup page
# Version 1.0
# Authors: Emma Carton (following tutorial)
# Dependencies: django library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
