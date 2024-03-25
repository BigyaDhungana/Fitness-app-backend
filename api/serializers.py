from rest_framework import serializers
from .models import AppUsers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppUsers
        fields=['username','email','password','profile_pic','first_name','last_name']

    def create(self, validated_data):
        print (validated_data)
        return AppUsers.objects.create_user(**validated_data)