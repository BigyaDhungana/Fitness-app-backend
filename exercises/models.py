from django.db import models
from django.utils import timezone
from api.models import AppUsers
# Create your models here.

focus_choices = (('abs','abs'),('shoulder_and_back','shoulder and back'),('chest','chest'),('legs','legs'),('arms','arms'))

class Exercises(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)
    focus=models.CharField(max_length=20,choices=focus_choices)
    gif=models.ImageField(upload_to='gifs')
    def __str__(self):
        return self.name
    
class PreDefinedWorkoutNames(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class PreDefinedWorkouts(models.Model):
    name=models.ForeignKey(PreDefinedWorkoutNames,on_delete=models.CASCADE)
    reps=models.IntegerField(null=True)
    time=models.IntegerField(null=True)
    exercise=models.ForeignKey(Exercises,on_delete=models.CASCADE)
    added_datetime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.name
 
class CustomWorkoutNames(models.Model):
    name=models.CharField(max_length=100)
    user=models.ForeignKey(AppUsers,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together=[['name','user']]

class CustomWorkouts(models.Model):
    workout=models.ForeignKey(CustomWorkoutNames,on_delete=models.CASCADE)
    reps=models.IntegerField(null=True)
    time=models.IntegerField(null=True)
    exercise=models.ForeignKey(Exercises,on_delete=models.CASCADE)
    added_datetime=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.workout.name