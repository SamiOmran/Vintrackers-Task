from rest_framework.serializers import ModelSerializer

from api.models.vehicle import Vehicle
from api.serializers.lead_serializer import ListLeadSerializer
from api.serializers.services_list_serializer import ListServiceSerializer


class VehicleSerializer(ModelSerializer):
    lead = ListLeadSerializer(required=False)

    class Meta:
        model = Vehicle
        fields = '__all__'


class ListVehicleSerializer(ModelSerializer):
    services = ListServiceSerializer(many=True, required=False)

    class Meta:
        model = Vehicle
        fields = ['id', 'model', 'vin', 'services']


class VehicleServiceSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['vin', 'model']
