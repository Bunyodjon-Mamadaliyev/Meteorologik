from rest_framework import serializers
from .models import Weather
from station.models import Station

class NestedStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name', 'station_id']

class WeatherSerializer(serializers.ModelSerializer):
    station = NestedStationSerializer(read_only=True)
    temperature = serializers.SerializerMethodField()
    humidity = serializers.SerializerMethodField()
    pressure = serializers.SerializerMethodField()
    wind_speed = serializers.SerializerMethodField()
    wind_direction = serializers.SerializerMethodField()
    precipitation = serializers.SerializerMethodField()

    def get_temperature(self, obj):
        return f"{obj.temperature:.1f}"

    def get_humidity(self, obj):
        return f"{obj.humidity:.1f}"

    def get_pressure(self, obj):
        return f"{obj.pressure:.1f}"

    def get_wind_speed(self, obj):
        return f"{obj.wind_speed:.1f}"

    def get_wind_direction(self, obj):
        return f"{obj.wind_direction:.1f}"

    def get_precipitation(self, obj):
        return f"{obj.precipitation:.1f}"

    class Meta:
        model = Weather
        fields = ['id', 'station', 'timestamp', 'temperature', 'humidity', 'pressure', 'wind_speed', 'wind_direction', 'precipitation', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class WeatherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['station', 'timestamp', 'temperature', 'humidity','pressure', 'wind_speed', 'wind_direction', 'precipitation']
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
