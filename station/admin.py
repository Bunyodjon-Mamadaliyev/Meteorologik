from django.contrib import admin
from .models import Station

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'station_id', 'latitude', 'longitude', 'elevation', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'station_id')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)
