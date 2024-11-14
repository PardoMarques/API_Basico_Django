from rest_framework import serializers
from .models import Car
from django.contrib.auth.models import User

class CarSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Car
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'cars']