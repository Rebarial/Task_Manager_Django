from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView
from allauth.account.views import SignupView, LoginView, PasswordResetView 


class MySignupView(SignupView):
    template_name = 'registration/register.html'

class MyLoginView(LoginView):
    template_name = 'account/login.html'

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = 'login/'

def register(request):
    return render(request, 'registration/register.html')

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'registration/logout.html')