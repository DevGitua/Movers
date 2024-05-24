booking/views.py

from django.shortcuts import render, redirect
from .models import Truck, Booking
from .forms import BookingForm

def home(request):
    trucks = Truck.objects.all()
    return render(request, 'booking/home.html', {'trucks': trucks})

def book_truck(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'booking/book_truck.html', {'form': form})