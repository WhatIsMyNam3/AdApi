from django.contrib.auth.models import User
from rest_framework.serializers import (
    CharField,
    EmailField,
    Serializer,
    ModelSerializer
)


class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class LoginSerializer(Serializer):
    email = EmailField()
    password = CharField(write_only=True)
