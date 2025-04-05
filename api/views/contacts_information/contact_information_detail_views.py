from api.models.contact_information import ContactInformation
from api.serializers.contact_information_serializer import ContactInformationSerializer
from api.views import get_object, APIView, Response, status


class ContactInformationDetailViews(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, contact_info):
        contact_info = get_object(ContactInformation, contact_info)
        serializer = ContactInformationSerializer(contact_info)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, contact_info):
        contact_info = get_object(ContactInformation, contact_info)
        serializer = ContactInformationSerializer(contact_info, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, contact_info):
        contact_info = get_object(ContactInformation, contact_info)
        contact_info.delete()

        return Response({'msg': 'model deleted'}, status=status.HTTP_200_OK)
