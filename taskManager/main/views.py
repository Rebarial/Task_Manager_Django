from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def index(request):
    #return redirect('/accounts/login')
    return render(request, 'main/index.html')

def logout_view(request):
    logout(request)

