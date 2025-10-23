from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name"]

    """ def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError("Email must contain @")
        return value.lower() """
