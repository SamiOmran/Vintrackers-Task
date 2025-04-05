from api.models.lead import Lead
from api.serializers.lead_serializer import LeadSerializer
from api.views import get_object, APIView, Response, status


class LeadDetailViews(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, lead):
        lead = get_object(Lead, lead)
        serializer = LeadSerializer(lead)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, lead):
        lead = get_object(Lead, lead)
        serializer = LeadSerializer(lead, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, lead):
        lead = get_object(Lead, lead)
        lead.delete()

        return Response('Model deleted', status=status.HTTP_200_OK)
