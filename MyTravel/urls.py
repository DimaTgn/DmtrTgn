from django.urls import path, include
from django.contrib import admin
from . views import home_view


urlpatterns = [
    path(r'admin', admin.site.urls, name='admin'),
    path(r'cities', include(('cities.urls', 'city'), namespace='city')),
    path(r'', home_view, name='home'),
]