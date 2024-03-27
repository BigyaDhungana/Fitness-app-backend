from django.urls import path
from . import views


urlpatterns = [
    path('get-exercises/',views.get_exercises,name="get_exercise"),
]