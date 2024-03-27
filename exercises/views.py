from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import Exercises
from .serializers import ExerciseSerializer
# Create your views here.

@api_view(['GET'])
def get_exercises(requset):
    """"
    Get all exercises
    """
    if (requset.user.is_authenticated):
        all_exercises=Exercises.objects.all()
        serialized_data=ExerciseSerializer(all_exercises,many=True)
        return Response(serialized_data.data,status=status.HTTP_200_OK)
    else:
        return Response({"error":"User not logged in"},status=status.HTTP_401_UNAUTHORIZED)

