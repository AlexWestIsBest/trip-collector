from django.shortcuts import render
from django.http import HttpResponse

class Trip:
    def __init__(self, place, age, story):
        self.place = place
        self.age = age
        self.story = story

trips = [
    Trip('Spain', 21, 'Visiting Barcelona'),
    Trip('Estonia', 22, 'Exploring the Baltics with friends'),
    Trip('Croatia', 23, 'Plus a small trip up to Croatia'),
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def trips_index(request):
    return render(request, 'trips/index.html', {'trips': trips})
