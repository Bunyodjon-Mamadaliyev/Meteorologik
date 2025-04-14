from rest_framework import serializers
from .models import Export

class ExportSerializer(serializers.ModelSerializer):
    export_type = serializers.ChoiceField(choices=Export.EXPORT_TYPE_CHOICES)
    status_display = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Export
        fields = ['id', 'export_type', 'status_display', 'user', 'created_at', 'completed_at',]
        read_only_fields = ['id', 'status_display', 'user', 'created_at', 'completed_at']

    def get_status_display(self, obj):
        return obj.get_status_display()

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
