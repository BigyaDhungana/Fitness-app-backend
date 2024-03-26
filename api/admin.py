from django.contrib import admin

# Register your models here.

from .models import AppUsers,UserDaily,UserDetails
from exercises.models import Exercises

class AppUsersAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','first_name','last_name','password']
class UserDetailsAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in UserDetails._meta.fields]
class ExerciseAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Exercises._meta.fields]

admin.site.register(AppUsers,AppUsersAdmin)
admin.site.register(Exercises,ExerciseAdmin)
admin.site.register(UserDaily)
admin.site.register(UserDetails,UserDetailsAdmin)
