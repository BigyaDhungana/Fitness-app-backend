from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
# Create your views here.

@api_view(['GET'])
def get_exercise(requset):
    """"
    Get all exercises
    """
    
    if (requset.user.is_authenticated):
        return Response({'success':"this works"},status=status.HTTP_200_OK)
    else:
        return Response({"error":"User not logged in"},status=status.HTTP_401_UNAUTHORIZED)

