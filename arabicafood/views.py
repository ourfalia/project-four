from django.shortcuts import render


def get_home(request):
    return render(request, 'arabicafood/home.html')

def make_reservation(request):
    return render(request, 'arabicafood/reservation.html')