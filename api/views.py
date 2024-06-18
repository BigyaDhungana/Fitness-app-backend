from django.shortcuts import render
from .models import AppUsers,UserDetails,UserDaily
from .serializers import UserSerializer,UserDetailsSerializer,UserDailySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from datetime import date,time,datetime
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
       

        user=authenticate(username=username,password=password)
        is_new_user=False
        if user is not None:
            token_tuple=Token.objects.update_or_create(user=user) #(token,created)
            # print(token_tuple)
            user_info=AppUsers.objects.get(username=username)

            try:
                user_detail=UserDetails.objects.get(user=user)
            
            except:
                is_new_user=True
            
            return Response({"username":user_info.username,"first_name":user_info.first_name,"last_name":user_info.last_name,"email":user_info.email,"profile_pic":"/media/"+str(user_info.profile_pic),"token":token_tuple[0].key,"is_new_user":is_new_user},status=status.HTTP_200_OK)
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
                if (request.data.get('gender') and request.data.get('height') and request.data.get('dob')):
                    user_detail,created=UserDetails.objects.update_or_create(user=request.user,defaults={"height":float(request.data['height']),"gender":request.data["gender"],"dob":request.data["dob"]})
                    
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
            

@api_view(['PUT'])
def update_user_daily(request):
    """Make a request once in a day to add user details to the database"""  
    if (request.user.is_authenticated):
        try:
            userDaily,created=UserDaily.objects.update_or_create(user=request.user,date=date.today(),
                    defaults={'steps':int(request.data['steps']),'calories':float(request.data['calories']),'water':int(request.data['water']),'weight':float(request.data['weight']),'sleep':float(request.data['sleep'])})
            return Response({"success":"Created or updated successfully"},status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({"error":"Bad request"},status=status.HTTP_400_BAD_REQUEST)
    else :
        return Response({"error":"User not logged in"},status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def get_data_for_graph(request):
    if (request.user.is_authenticated):
        print(datetime.now())
        try:
            usersinfo=UserDaily.objects.filter(user=request.user).order_by('date')[:30]
            serialized_data=UserDailySerializer(usersinfo,many=True)
            return Response(serialized_data.data,status=status.HTTP_200_OK)
        except:
            pass 
    else :
        return Response({"error":"User not logged in"},status=status.HTTP_401_UNAUTHORIZED)
        