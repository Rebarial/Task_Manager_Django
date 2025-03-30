from .tools.dateTimeManager import DateManager

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TasksForm
from django.views.generic import CreateView

from . import api
import requests


@login_required
def addTask(request):
    error = ''
    form = TasksForm()
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            try:
                new_submit = form.save(commit=False)
                new_submit.user_id = request.user.id
                new_submit.save()
                return redirect('planner')
            except:
                error = f'Данные были введены не верно'
                form.add_error(None, error)

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'planner/addTask.html', data)

@login_required
def index(request):

    responce = api.TaskViewSet

    tasks = responce.get_tasks_for_user(request.user)

    if ('date' in request.GET):
        date = request.GET['date']
        if date == '':
            date = DateManager.getCurrentDateTime()
        else:
            date = DateManager.getDataFromStr(date)

        weekday = []
    
        if (request.GET['action'] == 'Last'):
            weekday = DateManager.getWeekDates(DateManager.getLastWeek(date))
        if (request.GET['action'] == 'Next'):
            weekday = DateManager.getWeekDates(DateManager.getNextWeek(date))
        if (request.GET['action'] == 'Select'):
            weekday = DateManager.getWeekDates(date)
    else:
        weekday = DateManager.getWeekDates(DateManager.getCurrentDateTime())

    return render(request, 'planner/index.html', {'weekday': weekday, 'tasks': tasks, 'username': request.user})
