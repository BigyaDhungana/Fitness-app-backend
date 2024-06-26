from rest_framework import serializers
from .models import AppUsers,UserDetails,UserDaily

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppUsers
        fields=['username','email','password','profile_pic','first_name','last_name']

    def create(self, validated_data):
        # print (validated_data)
        return AppUsers.objects.create_user(**validated_data)
    
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetails
        exclude=['user']

class UserDailySerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDaily
        exclude=['user']