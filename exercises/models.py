from django.db import models

# Create your models here.

focus_choices = (('abs','abs'),('shoulder_and_back','shoulder and back'),('chest','chest'),('legs','legs'),('arms','arms'))

class Exercises(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)
    focus=models.CharField(max_length=20,choices=focus_choices)
    gif=models.ImageField(upload_to='gifs')

    def __str__(self):
        return self.name
    
