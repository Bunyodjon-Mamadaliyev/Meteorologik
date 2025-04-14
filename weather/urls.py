from django.urls import path
from .views import (
    WeatherDataListCreateView,
    WeatherDataRetrieveUpdateDestroyView,
    WeatherSearchView,
)

urlpatterns = [
    path('weather/', WeatherDataListCreateView.as_view(), name='weather-data-list'),
    path('weather/<int:pk>/', WeatherDataRetrieveUpdateDestroyView.as_view(), name='weather-data-detail'),
    path('weather/search/', WeatherSearchView.as_view(), name='weather-data-search'),
]