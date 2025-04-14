from rest_framework import serializers
from .models import Station

class StationSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    class Meta:
        model = Station
        fields = ['id', 'name', 'station_id', 'latitude', 'longitude',
                  'elevation', 'is_active', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data.pop('created_by', None)
        return super().create(validated_data)

