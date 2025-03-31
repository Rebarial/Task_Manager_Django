from django.db import models
from django.contrib.auth.models import User
import datetime
from .tools.dateTimeManager import DateManager

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Title',max_length=50)
    announce = models.CharField('Announce',max_length=250)
    date = models.DateField('Date', blank=True, default=DateManager.getCurrentDate())
    time = models.TimeField('Time', blank=True, default=DateManager.getCurrentTime())
    description = models.TextField('Description', blank=True, default="")

    def __str__(self):
        return  self.title
