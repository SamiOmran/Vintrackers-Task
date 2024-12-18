from rest_framework.serializers import ModelSerializer

from api.all_models.lead import Lead


class LeadSerializer(ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
