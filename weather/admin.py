from django.contrib import admin
from .models import Weather

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = (
        'station', 'timestamp', 'temperature', 'humidity',
        'pressure', 'wind_speed', 'wind_direction', 'precipitation', 'created_at'
    )
    list_filter = ('station', 'timestamp')
    search_fields = ('station__name',)
    readonly_fields = ('created_at',)
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)
