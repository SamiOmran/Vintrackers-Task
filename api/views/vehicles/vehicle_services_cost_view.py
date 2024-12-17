from django.db.models import Sum

from api.models import Service
from api.views import APIView, Response, status


class VehicleServicesCostView(APIView):
    def get(self, request, vehicle):
        costs = Service.objects.filter(vehicle_id=vehicle).aggregate(Sum('cost'))

        return Response(costs, status=status.HTTP_200_OK)
