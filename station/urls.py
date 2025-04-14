from django.urls import path
from .views import StationListCreateView, StationDetailView

urlpatterns = [
    path('stations/', StationListCreateView.as_view(), name='station-list'),
    path('stations/<int:pk>/', StationDetailView.as_view(), name='station-detail'),
]
