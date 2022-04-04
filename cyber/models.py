from django.db import models
class Game(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    description = models.TextField()
    release_date = models.DateTimeField()
# Create your models here.
