from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm, AuthForm
from django.contrib.auth import logout, login


class CreateUser(CreateView):
    form_class = RegisterForm
    template_name = 'client/create_user.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthForm
    template_name = 'client/login_user.html'

    def get_success_url(self):
        return '/'
