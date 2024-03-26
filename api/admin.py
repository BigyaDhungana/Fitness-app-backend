from django.contrib import admin

# Register your models here.

from .models import AppUsers,Exercises,UserDaily,UserDetails

class AppUsersAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','first_name','last_name','password']
class UserDetailsAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in UserDetails._meta.fields]

admin.site.register(AppUsers,AppUsersAdmin)
admin.site.register(Exercises)
admin.site.register(UserDaily)
admin.site.register(UserDetails,UserDetailsAdmin)
