from django.contrib import admin

# Register your models here.

from .models import AppUsers

class AppUsersAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','first_name','last_name','password']
    # search_fields = ['username','email','first_name','last_name']
    # list_filter = ['username','email','first_name','last_name']

admin.site.register(AppUsers,AppUsersAdmin)
