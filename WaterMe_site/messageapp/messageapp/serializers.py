from rest_framework import serializers
from .models import Message, SensorData, Plant


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['temperature','humidity']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['plant','created_at','sender','receiver','message']

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['plantid', 'plantName']
