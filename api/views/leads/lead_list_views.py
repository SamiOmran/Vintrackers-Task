from api.models import Lead
from api.serializers.lead_serializer import LeadSerializer
from api.views import APIView, Response, status


class LeadListViews(APIView):

    def get(self, request):
        data = Lead.objects.all()
        leads = LeadSerializer(data, many=True)

        return Response(leads.data, status=status.HTTP_200_OK)

    def post(self, request):
        lead = LeadSerializer(data=request.data)

        if lead.is_valid():
            lead.save()
            return Response(lead.data, status=status.HTTP_201_CREATED)

        return Response(lead.errors, status=status.HTTP_400_BAD_REQUEST)
