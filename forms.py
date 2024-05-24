from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'customer_name', 
            'customer_phone', 
            'pickup_address', 
            'dropoff_address', 
            'truck', 
            'date', 
            'time', 
            'items_description'
        ]