from django.urls import path, include
from . views import *

urlpatterns = [
    path('students/<int:ID>', view_getByID_updateByID_deleteByID)
]