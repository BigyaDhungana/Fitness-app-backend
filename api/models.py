from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class AppUsers(AbstractUser):
    profile_pic=models.ImageField(upload_to='users')

    def __str__(self):
        return self.username
    
class UserDetails(models.Model):
    user=models.OneToOneField(AppUsers,on_delete=models.CASCADE,primary_key=True)
    height=models.DecimalField(null=True,max_digits=5,decimal_places=2)#cm 
    gender=models.CharField(null=True,max_length=10)

    def __str__(self):
        return self.user.username

class UserDaily(models.Model):
    user=models.ForeignKey(AppUsers,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    steps=models.IntegerField(default=0)
    calories=models.DecimalField(default=0,max_digits=10,decimal_places=3)
    water=models.IntegerField(default=0)#in ml
    weight=models.DecimalField(null=True,max_digits=5,decimal_places=2)

    def __str__(self):
        return self.user.username