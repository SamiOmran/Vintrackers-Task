from api.views import APIView, Response, status
from api.serializers.service_serializer import ServiceSerializer
from api.models.service import Service


class ServiceTopFiveView(APIView):
    def get(self, request):
        top_5 = Service.objects.order_by('-cost').all()[:5]
        services = ServiceSerializer(top_5, many=True)

        return Response(services.data, status=status.HTTP_200_OK)
