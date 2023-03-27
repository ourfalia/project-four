from django.contrib import admin
from django.urls import path
from arabicafood.views import get_home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name='get_home'),
]
