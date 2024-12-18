from django.db.models import Sum

from api.all_models.service import Service
from api.views import APIView, Response, status


class TotalCostServicesView(APIView):
    def get(self, request):
        date = request.GET.get('date')
        if date:
            services = Service.objects.filter(date=date).aggregate(total_cost=Sum('cost'))
        else:
            services = Service.objects.aggregate(total_cost=Sum('cost'))

        return Response(services, status=status.HTTP_200_OK)
