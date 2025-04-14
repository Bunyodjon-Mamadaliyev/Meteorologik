from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Weather
from .serializers import WeatherSerializer, WeatherCreateSerializer
from common.permissions import IsOwnerOrAdmin
from .filters import WeatherFilter

class WeatherDataListCreateView(generics.ListCreateAPIView):
    queryset = Weather.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = WeatherFilter
    search_fields = [
        'station__name',
        'station__station_id',
        'wind_direction'
    ]
    ordering_fields = ['timestamp', 'temperature', 'created_at']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WeatherCreateSerializer
        return WeatherSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class WeatherDataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

class WeatherSearchView(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'station__name',
        'station__station_id',
        'wind_direction'
    ]