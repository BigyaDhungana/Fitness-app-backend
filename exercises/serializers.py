from rest_framework.serializers import ModelSerializer
from .models import Exercises,CustomWorkoutNames,PreDefinedWorkoutNames,PreDefinedWorkouts,CustomWorkouts

class ExerciseSerializer(ModelSerializer):
    class Meta:
        model=Exercises
        fields="__all__"

class CustomWorkoutNameSerializer(ModelSerializer):
    class Meta:
        model=CustomWorkoutNames
        fields="__all__"

class PreDefinedWorkoutNamesSeriallizer(ModelSerializer):
    class Meta:
        model=PreDefinedWorkoutNames
        fields='__all__'

class CustomWorkoutSerializer(ModelSerializer):
    class Meta:
        model=CustomWorkouts
        fields='__all__'

class PreDefinedWorkoutSerializer(ModelSerializer):
    class Meta:
        model=PreDefinedWorkouts
        exclude=['added_datetime','name']