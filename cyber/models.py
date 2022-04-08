from django.db import models
from django.contrib.auth.models import User
class User(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
class Game(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    description = models.TextField()
    release_date = models.DateTimeField()
# Create your models here.
