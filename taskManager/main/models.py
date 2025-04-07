from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icon = models.ImageField(blank=True)
    desctiption = models.TextField()
    def __str__(self):
        return self.user