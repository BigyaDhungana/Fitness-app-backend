from rest_framework.serializers import ModelSerializer
from .models import Exercises

class ExerciseSerializer(ModelSerializer):
    class Meta:
        model=Exercises
        exclude=['id']