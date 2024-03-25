from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

difficlty_choices = (('easy','easy'),('medium','medium'),('hard','hard'))
focus_choices = (('upper','upper'),('lower','lower'),('full','full'))

class Exercises(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)
    focus=models.CharField(max_length=10,choices=focus_choices)
    reps=models.JSONField()
    calories_burnt=models.JSONField()

    def __str__(self):
        return self.name

class AppUsers(AbstractUser):
    profile_pic=models.ImageField(upload_to='users')

    def __str__(self):
        return self.username