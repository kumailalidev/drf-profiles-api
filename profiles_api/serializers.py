from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "password")  # password field is optional
        extra_kwargs = {
            "password": {
                "write_only": True,  # Can not use to retrieve (GET) objects.
                "style": {"input_type": "password"},
            }
        }

    # - Overriding a default create function of ModelSerializer to create objects;
    #   Instead of using default create function it should use create_user function
    #   of model UserProfile to create user objects and create a password as a HASH
    #   instead of plan text.
    def create(self, validate_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validate_data["email"],
            name=validate_data["name"],
            password=validate_data["password"],
        )

        return user
