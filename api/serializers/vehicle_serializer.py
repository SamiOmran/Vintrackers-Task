from rest_framework.serializers import ModelSerializer

from api.all_models.vehicle import Vehicle


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class ListVehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'model', 'vin']


class VehicleServiceSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['vin', 'model']
