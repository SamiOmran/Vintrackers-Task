from api.models import Vehicle
from api.serializers.vehicle_serializer import VehicleSerializer
from api.views import get_object, APIView, Response, status


class VehicleDetailViews(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request, vehicle):
        vehicle = get_object(Vehicle, vehicle)
        serializer = VehicleSerializer(vehicle)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, vehicle):
        vehicle = get_object(Vehicle, vehicle)
        serializer = VehicleSerializer(vehicle, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vehicle):
        vehicle = get_object(Vehicle, vehicle)
        vehicle.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
