import json
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from tokens.models import BadToken
from tokens.authentication import BadTokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class CustomObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        username = request.data["username"]
        print(username)
        token = BadToken(username)
        key = token.__str__()
        return Response({'token': key})


class AuthenticatedView(APIView):
    authentication_classes = (BadTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response("Halloo!")
