from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


def get_object(model, id):
    try:
        return model.objects.get(pk=id)
    except model.DoesNotExist:
        raise Http404
