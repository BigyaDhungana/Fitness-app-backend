from django.urls import path
from . import views


urlpatterns = [
    path("exercises/",views.exercise_view,name="exercises")
    ,path("home/",views.home,name="home"),
    path("edit-exercises/",views.create_edit_exercises,name="get-edit-exercises")
]