from django.shortcuts import render
from .models import Reservation
from .forms import ReserveTableForm
from reservation.models import Reservation

# Create your views here.

def reserve_table(request):
    reserve_form = ReserveTableForm()
    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.method)
        if reserve_from.is_Valid():
            reserve_form.save()

    context = {'form' : reserve_form}

    return render(request, 'reservation/reservation.html', context)

