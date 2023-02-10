from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

VEHICLES = (
    ('F', 'Flight'),
    ('R', 'Roadtrip'),
    ('C', 'Cruise'),
)

# Create your models here.
class Companion(models.Model):
    name = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('companion_detail', kwargs={'pk': self.id})


class Trip(models.Model):
    place = models.CharField(max_length=50)
    age = models.IntegerField()
    story = models.TextField(max_length=250)
    companions = models.ManyToManyField(Companion)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.place

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trip_id': self.id})

class Transport(models.Model):
    date = models.DateField('Travel Date')
    vehicle = models.CharField(max_length=1, choices=VEHICLES, default=VEHICLES[0][0])
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_vehicle_display()} on {self.date}'

    class Meta:
        ordering = ['-date']