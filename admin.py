# booking/admin.py

from django.contrib import admin
from .models import Truck, Booking

admin.site.register(Truck)
admin.site.register(Booking)