from api.models.mechanic import Mechanic
from api.serializers.mechanic_serializer import MechanicSerializer
from api.views import get_object, APIView, Response, status


class MechanicDetailViews(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, mechanic):
        mechanic = get_object(Mechanic, mechanic)
        serializer = MechanicSerializer(mechanic)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, mechanic):
        mechanic = get_object(Mechanic, mechanic)
        serializer = MechanicSerializer(mechanic, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, mechanic):
        mechanic = get_object(Mechanic, mechanic)
        mechanic.delete()

        return Response({'msg': 'model deleted'}, status=status.HTTP_200_OK)
