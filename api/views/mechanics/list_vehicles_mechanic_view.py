from api.models import Mechanic
from api.serializers.vehicle_serializer import VehicleServiceSerializer
from api.views import APIView, Response, status, get_object


class ListVehiclesMechanicView(APIView):
    def get(self, request, mechanic):
        # first retrieve the services that mechanic worked on
        services = get_object(Mechanic, mechanic).services.all()
        # retrieve vehicles related to each service
        vehicles = [VehicleServiceSerializer(service.vehicle).data for service in services]

        return Response(vehicles, status=status.HTTP_200_OK)
