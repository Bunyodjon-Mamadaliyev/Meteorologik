import django_filters
from .models import Weather


class WeatherFilter(django_filters.FilterSet):
    min_temperature = django_filters.NumberFilter(field_name="temperature", lookup_expr='gte')
    max_temperature = django_filters.NumberFilter(field_name="temperature", lookup_expr='lte')
    date_from = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    date_to = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = Weather
        fields = {
            'station': ['exact'],
            'wind_direction': ['exact'],
            'humidity': ['gte', 'lte'],
            'precipitation': ['gte', 'lte'],
        }