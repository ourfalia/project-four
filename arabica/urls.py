from django.contrib import admin
from django.urls import path
from arabicafood.views import get_home
from reservation.views import reserve_table, my_reservation, confirmation, edit_item, cancel_item, cancelation


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name='get_home'),
    path('home/', get_home, name='home'),
    path('reservation/', reserve_table, name='reservation'),
    path('bookings/', my_reservation, name='bookings'),
    path('confirmation/', confirmation, name='confirmation'),
    path('edit/<item_id>', edit_item, name='edit'),
    path('cancel/<item_id>', cancel_item, name='cancel'),
    path('cancelation/', cancelation, name='cancelation'),
]
