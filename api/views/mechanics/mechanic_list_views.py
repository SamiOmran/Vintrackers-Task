from api.models.mechanic import Mechanic
from api.serializers.mechanic_serializer import MechanicSerializer
from api.views import APIView, Response, status


class MechanicListViews(APIView):

    def get(self, request):
        data = Mechanic.objects.all()
        mechanics = MechanicSerializer(data, many=True)

        return Response(mechanics.data, status=status.HTTP_200_OK)

    def post(self, request):
        mechanic = MechanicSerializer(data=request.data)

        if mechanic.is_valid():
            mechanic.save()
            return Response(mechanic.data, status=status.HTTP_201_CREATED)

        return Response(mechanic.errors, status=status.HTTP_400_BAD_REQUEST)
