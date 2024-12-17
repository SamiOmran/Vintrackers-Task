from rest_framework.serializers import ModelSerializer
from ..models import ContactInformation


class ContactInformationSerializer(ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'
