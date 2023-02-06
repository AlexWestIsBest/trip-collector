from django.db import models
from django.urls import reverse

# Create your models here.
class Companions(models.Model):
    name = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('companions_detail', kwargs={'pk': self.id})


class Trip(models.Model):
    place = models.CharField(max_length=50)
    age = models.IntegerField()
    story = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trip_id': self.id})

