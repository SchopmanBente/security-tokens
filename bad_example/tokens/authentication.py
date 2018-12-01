from rest_framework.authentication import TokenAuthentication
from bad_example.tokens.models import BadToken


class BadTokenAuthentication(TokenAuthentication):
    model = BadToken


