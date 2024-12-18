from rest_framework.serializers import ModelSerializer
from api.all_models.vehicle import Vehicle


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
