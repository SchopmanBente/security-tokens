from django.shortcuts import render
from django.tokens.authentication import BadTokenAuthentication

# Create your views here.
class MyView:
    authentication_classes = (BadTokenAuthentication)