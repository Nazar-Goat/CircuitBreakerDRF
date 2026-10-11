from rest_framework import serializers

from api.models import Service


class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "url",
            "failure_threshold",
            "reset_time",
            "created_at"
        ]
        read_only_fields = ["id", "created_at"]