from django.urls import path
from . import views


urlpatterns = [
    path('get-exercises/',views.get_exercises,name="get_exercise"),
    path('custom-workouts/',views.custom_workouts,name="custom_workouts"),
    path('get-predefined-workouts/',views.get_predefined_workouts,name='get_predefined_workouts'),
    path('get-ex-in-workout/',views.get_ex_in_workout,name='get_ex_in_workout'),
    path('add-ex-to-workout/',view=views.add_ex_to_workout,name='add_ex_to_workout'),
    path('remove-ex-from-workout/',views.remove_ex_from_workout,name='remove_ex_from_workout'),
    path('delete-workout/',views.delete_custom_workout,name='delete_workout'),
]