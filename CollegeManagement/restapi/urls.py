from django.urls import path, include
from . views import *

urlpatterns = [
    path('studentdata/',view_student_lists),
    path('studentdata/edit/<int:ID>',view_studentdata_updateform),
    path('studentdata/edit/update/<int:ID>',view_update_form_data_in_db),
    path('students/<int:ID>', view_updateByID)
]