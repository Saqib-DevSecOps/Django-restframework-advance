from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from src.accounts.models import User


class CustomUserCreateSerializer(UserCreateSerializer):
    email = serializers.EmailField(max_length=300,help_text='email should be unique and valid')
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password']
