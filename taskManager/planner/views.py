import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Task
from django.contrib.auth.models import User
from time import strptime
# Create your views here.


@login_required
def index(request):
    tasks = Task.objects.all().filter(user = request.user).order_by('data','time')
    weekday_name = ['Понедельник', 'Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
    if ('date' in request.GET):
        date = request.GET['date']
        if date == '':
            date = datetime.datetime.now()
        else:
            date = datetime.datetime.strptime(date,'%Y-%m-%d')
        if (request.GET['action'] == 'Last'):
            print(date.weekday())
            monday = (date -
                      datetime.timedelta(7-date.weekday()))
        if (request.GET['action'] == 'Next'):
            monday = (date +
                      datetime.timedelta(7-date.weekday()))
        if (request.GET['action'] == 'Select'):
            monday = (date -
                      datetime.timedelta(date.weekday()))
    else:
        monday = datetime.datetime.now() - datetime.timedelta(datetime.datetime.now().weekday())
        print(monday)
    weekdata = []
    for i in range(7):
        weekdata.append((monday + datetime.timedelta(i)).date())

    weekday = list(zip(weekday_name, weekdata))
    return render(request, 'planner/index.html', {'weekday': weekday, 'tasks': tasks, 'username': request.user})