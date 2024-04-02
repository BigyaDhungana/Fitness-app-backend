from django.urls import path
from . import views


urlpatterns = [
    path("exercises/",views.exercise_view,name="exercises")
    ,path("home/",views.home,name="home"),
    path("create-exercises/",views.create_exercises,name="create-exercises")
    ,path("edit-exercise/<str:id>",views.edit_exercise,name="edit-exercise"),
    path("delete-exercise/<str:id>",views.delete_exercise,name="delete-exercise"),
    path("all-workouts/",views.all_workouts,name="all-workouts"),
    path("create-workout/",views.create_workout,name="create-workout"),
]