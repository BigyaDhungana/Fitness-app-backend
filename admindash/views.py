from django.shortcuts import render,redirect
from .forms import AddExerciseForm
from exercises.models import Exercises
# Create your views here.

def exercise_view(request):
    all_exercises=Exercises.objects.all()
    context={"exercise_list":all_exercises}
    # print(all_exercises[0].name)
    return render(request,"exercises.html",context=context)

def home(request):
    return render(request,"home.html")

def create_edit_exercises(request):
    form=AddExerciseForm()
    context={"form":form}

    if request.method=="POST":
        form=AddExerciseForm(request.POST,request.FILES)
        print("----------------------------------------------------------------")
        if form.is_valid():
            form.save()
            return redirect("exercises")
        else:
            print(form.errors)


    return render(request,"exercise_form.html",context)
