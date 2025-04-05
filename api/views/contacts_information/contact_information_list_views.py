from api.models.contact_information import ContactInformation
from api.serializers.contact_information_serializer import ContactInformationSerializer
from api.views import APIView, Response, status


class ContactInformationListViews(APIView):

    def get(self, request):
        data = ContactInformation.objects.all()
        contacts_info = ContactInformationSerializer(data, many=True)

        return Response(contacts_info.data, status=status.HTTP_200_OK)

    def post(self, request):
        contact_info = ContactInformationSerializer(data=request.data)

        if contact_info.is_valid():
            contact_info.save()
            return Response(contact_info.data, status=status.HTTP_201_CREATED)

        return Response(contact_info.errors, status=status.HTTP_400_BAD_REQUEST)
