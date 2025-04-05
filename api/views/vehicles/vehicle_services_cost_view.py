from django.db.models import Sum

from api.models.service import Service
from api.views import APIView, Response, status


class VehicleServicesCostView(APIView):
    def get(self, request, vehicle):
        costs = Service.objects.filter(vehicle_id=vehicle).aggregate(total_cost=Sum('cost'))

        return Response(costs, status=status.HTTP_200_OK)
