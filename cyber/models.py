from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Games(models.Model):
    name = models.CharField(max_length=100)
    developer = models.ForeignKey(User, on_delete = models.CASCADE)
    genre = models.CharField(max_length=30)
    description = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now, blank = True)
    release_date = models.DateTimeField()
    # image = models.FileField(upload_to=filepath,)
    def __str__(self):
        return self.name
# class Developer (models.Model):
#     name = models.CharField(max_length=100)
#     game = models.ForeignKey(Games, on_delete = models.CASCADE)
#     description = models.TextField()
#     date_joined = models.DateTimeField(default = timezone.now, blank = True)
#     # image = models.FileField(upload_to=filepath,)
# Create your models here.
