from rest_framework.serializers import ModelSerializer

from api.serializers.vehicle_serializer import VehicleSerializer
from api.models.service import Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ListVehicleServiceSerializer(ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = Service
        fields = ['cost', 'vehicle']
