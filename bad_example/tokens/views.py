from django.shortcuts import render
import json
from rest_framework.authtoken.views import ObtainAuthToken
from tokens.models import BadToken
from rest_framework.response import Response


# Create your views here.


class CustomObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = BadToken()
        key = token.__str__()
        return Response({'token': key})
