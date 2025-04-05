from api.models.lead import Lead
from api.models.vehicle import Vehicle
from api.serializers.lead_serializer import LeadSerializer
from api.serializers.vehicle_serializer import ListVehicleSerializer
from api.views import get_object, APIView, Response, status


class LeadVehiclesView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, lead):
        # lead = get_object(Lead, lead)
        vehicles = Vehicle.objects.filter(lead=lead).all()

        serializer = ListVehicleSerializer(vehicles, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
