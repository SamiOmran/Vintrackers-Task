from django.db.models import Sum

from api.models.lead import Lead
from api.models.service import Service
from api.models.vehicle import Vehicle
from api.views import APIView, Response, get_object, status


class VehicleCostPerLeadView(APIView):
    def get(self, request, lead):
        found = get_object(Lead, lead)
        if found:
            vehicles = Vehicle.objects.filter(lead=lead)
            cost = Service.objects.filter(vehicle__in=vehicles).aggregate(total_cost=Sum('cost'))['total_cost'] or 0
            total = {'total_cost': cost}

            return Response(total, status=status.HTTP_200_OK)
