from rest_framework.serializers import ModelSerializer

from api.models.service import Service


class ListServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'cost']
