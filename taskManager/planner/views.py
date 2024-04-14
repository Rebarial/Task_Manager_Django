import datetime

from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import api
import requests

@login_required
def index(request):

    responce = api.TaskViewSet

    tasks = responce.get_tasks_for_user(request.user)

    weekday_name = ['Понедельник', 'Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
    if ('date' in request.GET):
        date = request.GET['date']
        if date == '':
            date = datetime.datetime.now()
        else:
            date = datetime.datetime.strptime(date,'%Y-%m-%d')
        if (request.GET['action'] == 'Last'):
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
    weekdate = []
    for i in range(7):
        weekdate.append((monday + datetime.timedelta(i)).date())

    weekday = list(zip(weekday_name, weekdate))
    return render(request, 'planner/index.html', {'weekday': weekday, 'tasks': tasks, 'username': request.user})
