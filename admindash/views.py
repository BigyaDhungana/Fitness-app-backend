from django.shortcuts import render

# Create your views here.

def exercise_view(request):
    return render(request,"exercises.html")

def home(request):
    return render(request,"home.html")
