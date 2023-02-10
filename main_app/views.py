from django.shortcuts import render, redirect
from .models import Trip, Companion
from .forms import TransportForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def trips_index(request):
    # trips = Trip.objects.all()
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trips/index.html', {'trips': trips})

@login_required
def trips_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    not_companions = Companion.objects.exclude(id__in = trip.companions.all().values_list('id'))
    transport_form = TransportForm()
    return render(request, 'trips/detail.html', {
        'trip': trip,
        'transport_form': transport_form,
        'companions': not_companions,
    })

@login_required
def add_transport(request, trip_id):
    form = TransportForm(request.POST)
    if form.is_valid():
        new_transport = form.save(commit=False)
        new_transport.trip_id = trip_id
        new_transport.save()
    return redirect('detail', trip_id=trip_id)

@login_required
def assoc_companion(request, trip_id, companion_id):
    Trip.objects.get(id=trip_id).companions.add(companion_id)
    return redirect('detail', trip_id=trip_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class TripCreate(LoginRequiredMixin, CreateView):
    model = Trip
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TripUpdate(LoginRequiredMixin, UpdateView):
    model = Trip
    fields = '__all__'

class TripDelete(LoginRequiredMixin, DeleteView):
    model = Trip
    success_url = '/trips/'

class CompanionIndex(LoginRequiredMixin, ListView):
    model = Companion

class CompanionDetail(LoginRequiredMixin, DetailView):
    model = Companion

class CompanionCreate(LoginRequiredMixin, CreateView):
    model = Companion
    fields = '__all__'

class CompanionUpdate(LoginRequiredMixin, UpdateView):
    model = Companion
    fields = '__all__'

class CompanionDelete(LoginRequiredMixin, DeleteView):
    model = Companion
    success_url = '/companions/'