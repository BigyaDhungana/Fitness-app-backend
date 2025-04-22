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
    dob=models.CharField(null=True,max_length=30)

    def __str__(self):
        return self.user.username

class UserDaily(models.Model):
    user=models.ForeignKey(AppUsers,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    steps=models.IntegerField(default=0)
    calories=models.DecimalField(default=0,max_digits=10,decimal_places=3)
    water=models.IntegerField(default=0)#in ml
    weight=models.DecimalField(null=True,max_digits=5,decimal_places=2)
    sleep=models.DecimalField(null=True,max_digits=5,decimal_places=2)#in hours

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return self.user.username
    
class OTP(models.Model):
    pass
    user=models.OneToOneField(AppUsers,on_delete=models.CASCADE)
    latest_otp=models.CharField(max_length=6) #cannot be int cause of possible leading zeros 
    created_at=models.DateTimeField(auto_now_add=True)