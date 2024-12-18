from rest_framework.serializers import ModelSerializer

from api.all_models.contact_information import ContactInformation


class ContactInformationSerializer(ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'


class LeadContactInfoSerializer(ModelSerializer):
    class Meta:
        model = ContactInformation
        exclude = ['lead_id']
