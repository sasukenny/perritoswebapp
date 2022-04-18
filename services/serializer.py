from rest_framework import serializers
from services.models import hired_service, service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = service
        fields = '__all__'
        

class HiredServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = hired_service
        fields = '__all__'