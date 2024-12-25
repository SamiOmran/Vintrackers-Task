from django.db.models import Count

from api.all_models.lead import Lead
from api.views import APIView, Response, status


class LeadCreatedDayView(APIView):
    def get(self, request):
        services = Lead.objects.extra({'created_day': 'date(created_at)'}).values('created_day').annotate(count=Count('created_at'))

        return Response(services, status=status.HTTP_200_OK)
