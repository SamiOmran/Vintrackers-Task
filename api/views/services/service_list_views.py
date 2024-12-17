from api.models import Service
from api.serializers.service_serializer import ServiceSerializer
from api.views import APIView, Response, status


class ServiceListViews(APIView):

    def get(self, request):
        data = Service.objects.all()
        services = ServiceSerializer(data, many=True)

        return Response(services.data, status=status.HTTP_200_OK)

    def post(self, request):
        service = ServiceSerializer(data=request.data)

        if service.is_valid():
            service.save()
            return Response(service.data, status=status.HTTP_201_CREATED)

        return Response(service.errors, status=status.HTTP_400_BAD_REQUEST)
