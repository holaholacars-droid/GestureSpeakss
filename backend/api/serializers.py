from .models import User, Agent, Service
from .serializers import BodyguardSerializer, UserSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone_no', 'location', 'created_at', 'is_active', 'is_verified']

class BodyguardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'name', 'email', 'phone_no', 'location', 'created_at', 'is_active', 'is_verified', 'experience_years', 'rating', 'is_available']

class ServiceSerializer(serializers.ModelSerializer):
    bodyguard = BodyguardSerializer()
    user = UserSerializer()

    class Meta:
        model = Service
        fields = ['id', 'bodyguard', 'user', 'service_date', 'location', 'description', 'is_completed']