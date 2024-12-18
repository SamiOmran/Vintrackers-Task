from rest_framework.serializers import ModelSerializer
from api.all_models.service import Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ListServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'cost']
