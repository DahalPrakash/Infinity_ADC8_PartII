from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    #index page and login, sign up, logout
    path('',get_isauthencitated_home,),
    path('signup/',view_register_user,name="signup"),
    path('login',view_authenticate_user,name="login"),
    path('logout',logout_user,name="logout"),
    
]