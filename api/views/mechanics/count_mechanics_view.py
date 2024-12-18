from django.db.models import Count

from api.models import Mechanic
from api.views import APIView, Response, status


class CountMechanicsView(APIView):
    def get(self, request):
        mechanics = Mechanic.objects.values('specialization').annotate(count=Count('specialization'))

        return Response(mechanics, status=status.HTTP_200_OK)
