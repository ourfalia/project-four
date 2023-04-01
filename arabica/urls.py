from django.contrib import admin
from django.urls import path
from arabicafood.views import get_home
from reservation import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name='get_home'),
    path('home/', get_home, name='home'),
    path('reservation/', views.reserve_table, name='reservation'),
    path('bookings/', views.my_reservation, name='bookings'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('cancel/<item_id>', views.cancel_item, name='cancel'),
    path('cancelation/', views.cancelation, name='cancelation'),
]
