from .views import home, CityDetailView
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
]
