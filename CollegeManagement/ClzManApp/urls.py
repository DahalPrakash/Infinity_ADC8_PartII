from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = "personal"

urlpatterns = [
    path('',views.home, name='home'),
    path('home.html',views.home, name='home'),
    path('academic.html',views.academic, name='academic'),
    path('contact.html',views.contact, name='contact'),
    path('about.html',views.about, name='about'),
    path('search.html',views.search, name='search'),
    path('admissionform.html', views.admissionform, name='admissionform'),
    #for pdf upload download
    path('fileupload.html', views.upload_file, name="upload"),
    path('filelist.html', views.list_file, name="list"),
    

]