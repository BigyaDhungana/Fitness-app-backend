from django.shortcuts import render,redirect
from .forms import AddExerciseForm,AddWorkoutNameForm,AddExerciseToWorkoutForm
from exercises.models import Exercises,PreDefinedWorkoutNames,PreDefinedWorkouts
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def exercise_view(request):
    all_exercises=Exercises.objects.all()
    context={"exercise_list":all_exercises}
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
            form=AddExerciseForm()
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
    if selected_id is None:
        param_present=False
        all_exercises_in_workout=""
    else :
        param_present=True
        all_exercises_in_workout=PreDefinedWorkouts.objects.filter(name=selected_id).order_by('added_datetime')
        
    workout_name_form=AddWorkoutNameForm()
    add_to_workout_form=AddExerciseToWorkoutForm()
    workouts=PreDefinedWorkoutNames.objects.all()
    try:
        if param_present:
            selected_workout=PreDefinedWorkoutNames.objects.get(id=selected_id)
            if request.method=="POST":
                add_to_workout_form=AddExerciseToWorkoutForm(request.POST)
                if add_to_workout_form.is_valid():
                    form_instance=add_to_workout_form.clean()
                    if form_instance['type']=='Reps':
                        time=None
                        reps=form_instance['reps']
                    else:
                        time=form_instance['reps']
                        reps=None
                    PreDefinedWorkouts.objects.create(name=selected_workout,exercise=form_instance['exercise'],reps=reps,time=time)
                    return redirect(reverse('all-workouts')+'?id='+str(selected_id))
    except:
        messages.error(request,"Invalid page request")
        return redirect('all-workouts')

    context={'workouts':workouts,"workout_name_form":workout_name_form,"add_to_workout_form":add_to_workout_form,'param_present':param_present,'selected_id':selected_id,'all_exercises':all_exercises_in_workout}
    return render(request,"allworkouts.html",context=context)

def create_workout(request):
    form=AddWorkoutNameForm()
    if request.method=="POST":
        form=AddWorkoutNameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all-workouts")
        else:
            messages.error(request,"Name already exists")
            return redirect('all-workouts')
    return redirect("all-workouts")

def delete_exercise_from_workout(request,id):
    try:
        workout_name_id=PreDefinedWorkouts.objects.get(id=id).name.id
        PreDefinedWorkouts.objects.get(id=id).delete()
    except:
        print()
        return HttpResponse("<h1>Something went wrong</h1>")
    return redirect(reverse("all-workouts")+f"?id={workout_name_id}")

def delete_workout(request,id):
    try:
        PreDefinedWorkoutNames.objects.get(id=id).delete()
    except:
        return HttpResponse("<h1>Something went wrong</h1>")
    return redirect("all-workouts")