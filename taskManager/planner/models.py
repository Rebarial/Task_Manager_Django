from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Title',max_length=50)
    announce = models.CharField('Announce',max_length=250)
    date = models.DateField('Date', blank=True, default=datetime.datetime.now().date())
    time = models.TimeField('Time', blank=True, default=datetime.datetime.now().time())
    description = models.TextField('Description', blank=True, default="")

    def __str__(self):
        return  self.title
