from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "created_at",
            "updated_at",
            "creator",
            "title",
            "description",
            "private",
            "tags",
            "topics",
        ]
