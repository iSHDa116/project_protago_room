from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from .forms import SignUpForm

# Create your views here.
class SignupView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "registration/singup.html"
    success_url = reverse_lazy('game_index')


class SignupDoneView(DeleteView):
    template_name = "registration/signup_done.html"