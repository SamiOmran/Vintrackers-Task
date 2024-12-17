from rest_framework.serializers import ModelSerializer
from ..models import Mechanic


class MechanicSerializer(ModelSerializer):
    class Meta:
        model = Mechanic
        fields = '__all__'
