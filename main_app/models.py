from django.db import models

# Create your models here.
class Trip(models.Model):
    place = models.CharField(max_length=50)
    age = models.IntegerField()
    story = models.TextField(max_length=250)