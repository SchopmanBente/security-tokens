from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from django.contrib.auth.models import User
import base64
from tokens.models import BadToken



class BadTokenAuthentication(TokenAuthentication):


    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            return None
        try:
            stringtodecode = token.replace("Token", "")
            answer = base64.b64decode(stringtodecode)
            answer2 = answer.decode("utf-8")
            if "userid=" in answer2:
                id = answer2.replace("userid=", "")
                user = User.objects.filter(pk=id).first()
            else:
                return None
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return (user, None)



