from django.shortcuts import render
from .models import Item


def get_home(request):
    return render(request, 'arabicafood/home.html')

def make_reservation(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'arabicafood/reservation.html', context)