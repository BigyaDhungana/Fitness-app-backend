from django.shortcuts import render
from .models import AppUsers,UserDetails
from .serializers import UserSerializer,UserDetailsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.

@api_view(['POST'])
def register(request):

    """
    REGISTER A USER

    username,email,password,profile_pic,first_name,last_name

    """
    if request.method=="POST":
        user_name=request.data['username']
        
        try :
            user=AppUsers.objects.get(username=user_name)
            return Response({"error":"User already exists"},status=status.HTTP_409_CONFLICT)
        except:
            selializer=UserSerializer(data=request.data)
            if selializer.is_valid():
                # print (selializer.validated_data)
                selializer.save()
                return Response({"success":"User created successfully"},status=status.HTTP_201_CREATED)
            else: 
                return Response(selializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['POST'])
def login_user(request):
    """
    Username login
    """
    if request.method=="POST":
        username=request.data['username']
        password=request.data['password']
        print(username,password)

        user=authenticate(username=username,password=password)
        
        if user is not None:
            token_tuple=Token.objects.update_or_create(user=user) #(token,created)
            # print(token_tuple)
            user_info=AppUsers.objects.get(username=username)
            return Response({"success":"Login successful","first_name":user_info.first_name,"last_name":user_info.last_name,"email":user_info.email,"profile_pic":"/media/"+str(user_info.profile_pic),"token":token_tuple[0].key},status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)

    


@api_view(['POST'])
def logout_user(request):
    """
    Logout
    """
    try :
        request.user.auth_token.delete()
        return Response({"success":"User logged out"},status=status.HTTP_200_OK)
    except:
        return Response({"error":"User not logged in"},status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT','GET'])
def add_user_details(request):
    """ 
    PUT: Route to add/modify users height or gender
    GET: Route to get user gender and height
    """
    if (request.method=="PUT"):
        try :
            if (request.user.is_authenticated):
                if (request.data.get('gender') and request.data.get('height')):
                    user_detail,created=UserDetails.objects.update_or_create(user=request.user,defaults={"height":float(request.data['height']),"gender":request.data["gender"]})
                    print(user_detail)
                    print("hi")
                return Response({"success":"true"})
            else :
                return Response({"error":"User not logged in"},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as error:
            print(error)
            return Response({"error":"Bad request"},status=status.HTTP_400_BAD_REQUEST)
        
    elif(request.method=="GET"):    
            if (request.user.is_authenticated):
                user_detail=UserDetails.objects.get(user=request.user)
                serializer=UserDetailsSerializer(user_detail,many=False)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response({"error":"User not logged in"},status=status.HTTP_401_UNAUTHORIZED)