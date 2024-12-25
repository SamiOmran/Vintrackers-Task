from api.models import Service
from api.serializers.service_serializer import ServiceSerializer
from api.views import get_object, APIView, Response, status


class ServiceDetailViews(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, service):
        service = get_object(Service, service)
        serializer = ServiceSerializer(service)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, service):
        service = get_object(Service, service)
        serializer = ServiceSerializer(service, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, service):
        service = get_object(Service, service)
        service.delete()

        return Response({'msg': 'model deleted'}, status=status.HTTP_200_OK)
