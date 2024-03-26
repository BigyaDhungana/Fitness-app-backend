from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register,name="register"),
    path('login/',views.login_user,name="login"),
    #path('get-exercises/',views.get_exercise,name="get_exercise"),
    path('logout/',views.logout_user,name="logout"),
    path('user-details/',views.add_user_details,name="user_details")
]