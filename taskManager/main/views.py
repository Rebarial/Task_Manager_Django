from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def logout_view(request):
    logout(request)

