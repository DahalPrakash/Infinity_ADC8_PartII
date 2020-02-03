from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home.html',views.home, name='home'),
    path('academic.html',views.academic, name='academic'),
    path('contact.html',views.contact, name='contact'),
    path('about.html',views.about, name='about'),
    path('search.html',views.search, name='search'),
    path('admissionform.html', views.admissionform, name='admissionform'),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

]