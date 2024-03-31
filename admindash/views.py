from django.shortcuts import render,redirect
from .forms import AddExerciseForm,AddWorkoutNameForm
from exercises.models import Exercises,PreDefinedWorkoutNames,PreDefinedWorkouts
from django.http import HttpResponse
# Create your views here.

def exercise_view(request):
    all_exercises=Exercises.objects.all()
    context={"exercise_list":all_exercises}
    # print(all_exercises[0].name)
    return render(request,"exercises.html",context=context)

def home(request):
    return render(request,"home.html")

def create_exercises(request):
    form=AddExerciseForm()
    context={"form":form}

    if request.method=="POST":
        form=AddExerciseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("exercises")
        else:
            print(form.errors)

    return render(request,"exercise_form.html",context)

def edit_exercise(request,id):
    exercise_instance=Exercises.objects.get(id=id)
    form=AddExerciseForm(instance=exercise_instance)

    if (request.method=="POST"):
        form=AddExerciseForm(request.POST,request.FILES,instance=exercise_instance)
        if form.is_valid():
            form.save()
            return redirect("exercises")

    context={"form":form}
    return render(request,"exercise_form.html",context=context)

def delete_exercise(request,id):
    try:
        Exercises.objects.get(id=id).delete()
    except:
        return HttpResponse("<h1>Something went wrong</h1>")
    return redirect("exercises")

def all_workouts(request):
    selected_id=request.GET.get('id')
    print(selected_id,"heh")
    workout_name_form=AddWorkoutNameForm()
    workouts=PreDefinedWorkoutNames.objects.all()
    context={'workouts':workouts,"workout_name_form":workout_name_form}
    return render(request,"allworkouts.html",context=context)