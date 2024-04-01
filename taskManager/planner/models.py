from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Title',max_length=50)
    announce = models.CharField('Announce',max_length=250)
    data = models.DateField('Data', blank=True)
    time = models.TimeField('Time', blank=True)
    description = models.TextField('Description', blank=True)

    def __str__(self):
        return  self.title
