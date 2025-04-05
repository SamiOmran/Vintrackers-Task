from api.models.vehicle import Vehicle
from api.serializers.vehicle_serializer import ListVehicleSerializer, VehicleSerializer
from api.views import APIView, Response, status


class VehicleListViews(APIView):

    def get(self, request):
        data = Vehicle.objects.prefetch_related('services').all()
        vehicles = ListVehicleSerializer(data, many=True)

        return Response(vehicles.data, status=status.HTTP_200_OK)

    def post(self, request):
        vehicle = VehicleSerializer(data=request.data)

        if vehicle.is_valid():
            vehicle.save()
            return Response(vehicle.data, status=status.HTTP_201_CREATED)

        return Response(vehicle.errors, status=status.HTTP_400_BAD_REQUEST)
