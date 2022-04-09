from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Game(models.Model):
    name = models.CharField(max_length=100)
    developer = models.ForeignKey(User, on_delete = models.CASCADE)
    genre = models.CharField(max_length=30)
    description = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now, blank = True)
    release_date = models.DateTimeField()
    def __str__(self):
        return self.name
# Create your models here.
