from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]

    def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError("Email must contain @")
        return value.lower()


