from rest_framework.serializers import ModelSerializer

from api.models.lead import Lead
from api.serializers.contact_information_serializer import LeadContactInfoSerializer


class LeadSerializer(ModelSerializer):
    contacts_information = LeadContactInfoSerializer(many=True, required=False)

    class Meta:
        model = Lead
        fields = '__all__'


class ListLeadSerializer(ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'first_name', 'last_name']
