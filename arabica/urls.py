from django.contrib import admin
from django.urls import path
from arabicafood.views import get_home
from reservation.views import  reserve_table, my_reservation


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name='get_home'),
    path('home/', get_home, name='home'),
    path('reservation/', my_reservation, name='reservation'),
    path('reservation/', reserve_table, name='reservation'),
]
