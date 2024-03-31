from django.contrib import admin

# Register your models here.

from .models import AppUsers,UserDaily,UserDetails
from exercises.models import Exercises,PreDefinedWorkoutNames,PreDefinedWorkouts

class AppUsersAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','first_name','last_name','password']
class UserDetailsAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in UserDetails._meta.fields]
class ExerciseAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Exercises._meta.fields]
class WorkoutNamesAdmin(admin.ModelAdmin):
    list_display=[f.name for f in PreDefinedWorkoutNames._meta.fields]
class PreWorkoutsAdmin(admin.ModelAdmin):
    list_display=[f.name for f in PreDefinedWorkouts._meta.fields]



admin.site.register(AppUsers,AppUsersAdmin)
admin.site.register(Exercises,ExerciseAdmin)
#admin.site.register(UserDaily)
admin.site.register(UserDetails,UserDetailsAdmin)
admin.site.register(PreDefinedWorkoutNames,WorkoutNamesAdmin)
admin.site.register(PreDefinedWorkouts,PreWorkoutsAdmin)
