from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import Exercises,CustomWorkoutNames,CustomWorkouts,PreDefinedWorkoutNames,PreDefinedWorkouts
from .serializers import ExerciseSerializer,CustomWorkoutNameSerializer,PreDefinedWorkoutNamesSeriallizer,CustomWorkoutSerializer,PreDefinedWorkoutSerializer
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


@api_view(['GET','POST'])##{"name":"haha"}
def custom_workouts(request):
    """
    Get all custom workouts
    Post create a custom workout
    """
    if (request.user.is_authenticated):
        if request.method=="GET":
            all_workouts=CustomWorkoutNames.objects.all()
            serialized_data=CustomWorkoutNameSerializer(all_workouts,many=True)
            return Response(serialized_data.data,status=status.HTTP_200_OK)
        elif request.method=="POST":
            try:
                workout_instance=CustomWorkoutNameSerializer(data={"name":request.data['name'],"user":request.user.id})
                if workout_instance.is_valid():
                    workout_instance.save()
                    return Response({"success":"workout created"},status=status.HTTP_201_CREATED)
                else:
                    return Response({"error":"name already exists"},status=status.HTTP_409_CONFLICT)
            except:
                return Response({"error":"Bad request"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error":"Invalid request"},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error":"User not logged in"},status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['GET'])
def get_predefined_workouts(request):
    """
    get all predefined workouts
    """
    if request.user.is_authenticated:
        serialized_data=PreDefinedWorkoutNamesSeriallizer(PreDefinedWorkoutNames.objects.all(),many=True)
        return Response(serialized_data.data,status=status.HTTP_200_OK)
    else:
        return Response({"error":"User not logged in"},status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
def get_ex_in_workout(request):#cid or pid
    """
    Get all exercises in a workout
    """
    if request.user.is_authenticated:
        query=request.query_params
        if "cid" in query:
            workouts=CustomWorkouts.objects.filter(workout=query['cid']).order_by("added_datetime")
            serlialized_data=CustomWorkoutSerializer(workouts,many=True)
 
        elif "pid" in query:
            workouts=PreDefinedWorkouts.objects.filter(name__id=query['pid']).order_by("added_datetime")
            serlialized_data=PreDefinedWorkoutSerializer(workouts,many=True)

        else:
            return Response({"error":"Invalid request"},status=status.HTTP_400_BAD_REQUEST)
        
        for workout,s_d in zip(workouts,serlialized_data.data):
            s_d['exercise']=ExerciseSerializer(workout.exercise).data       
            
        return Response(serlialized_data.data,status=status.HTTP_200_OK)
     
    else:
        return Response({"error":"User not logged in"},status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
def add_ex_to_workout(request):#wid eid
    """
    Add exercise to a workout 
    request body workout id and exercise id
    """
    if request.user.is_authenticated:
        try:
            if "wid" in request.data and "eid" in request.data:
                workout=CustomWorkoutNames.objects.get(id=int(request.data['wid']))
                exercise=Exercises.objects.get(id=int(request.data['eid']))
                CustomWorkouts.objects.create(workout=workout,reps=int(request.data['quantity']) if "is_reps" else None,time=None if request.data["is_reps"] else int(request.data['quantity']) ,exercise=exercise )
                return Response({"success":"true"},status=status.HTTP_201_CREATED)
            else:
                return Response({"error":"Bad request"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print(error)
            return Response({"error":"Bad request"},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error":"User not logged in"},status=status.HTTP_401_UNAUTHORIZED)