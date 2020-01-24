from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home.html',views.home, name='home'),
    path('students.html',views.students, name='students'),
    path('staff.html',views.staff, name='staff'),
    path('contact.html',views.contact, name='contact'),
    path('about.html',views.about, name='about'),
    path('search.html',views.search, name='search'),

]