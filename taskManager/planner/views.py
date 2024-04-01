import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Task
from django.contrib.auth.models import User
# Create your views here.


@login_required
def index(request):
    tasks = Task.objects.all().filter(user = request.user).order_by('data','time')
    print(request.GET.get('param1', None))
    print(request.user)
    print(tasks)
    monday = datetime.datetime.now() - datetime.timedelta(datetime.datetime.now().weekday()+7)
    weekday = []
    for i in range(7):
        weekday.append((monday + datetime.timedelta(i)).date())
    return render(request, 'planner/index.html', {'weekday': weekday, 'tasks': tasks})