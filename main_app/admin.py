from django.contrib import admin
from .models import Trip, Companion, Transport

# Register your models here.
admin.site.register(Trip)
admin.site.register(Companion)
admin.site.register(Transport)