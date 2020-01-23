from django.urls import path, include
from . views import *

urlpatterns = [
    path('search/', search),
    path('studentdata/',view_student_lists),
    path('studentform/',view_student_form),
    path('studentform/save',view_studentdata_save),
    path('studentdata/edit/<int:ID>',view_studentdata_updateform),
    path('studentdata/edit/update/<int:ID>',view_update_form_data_in_db),
]