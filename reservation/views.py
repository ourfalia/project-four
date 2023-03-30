from django.shortcuts import render
from.models import Reservation
from reservation.models import Reservation

# Create your views here.

def reserve_table(request):
    return render(request, 'reservation/reservation.html')
