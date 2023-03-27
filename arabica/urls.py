from django.contrib import admin
from django.urls import path
from arabicafood.views import get_home, make_reservation


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name='get_home'),
    path('home', get_home, name='home'),
    path('reservation', make_reservation, name='reservation'),
]
