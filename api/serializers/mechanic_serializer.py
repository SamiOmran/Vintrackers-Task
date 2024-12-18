from rest_framework.serializers import ModelSerializer

from api.all_models.mechanic import Mechanic


class MechanicSerializer(ModelSerializer):
    class Meta:
        model = Mechanic
        fields = '__all__'
