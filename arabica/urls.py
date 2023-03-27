from django.contrib import admin
from django.urls import path
from arabicafood.views import get_home, make_reservation


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', make_reservation, name='reservation'),
    path('', get_home, name='get_home'),
]
