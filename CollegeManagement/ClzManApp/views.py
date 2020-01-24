from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.template import Template, Context
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# for register login logout sign up all function are below
def get_isauthencitated_home(request):
    if request.user.is_authenticated:
        return render(request,"registration/home.html")
    else:
        return redirect('login')

def view_register_user(request):
    if request.method == "GET":
        return render(request, 'registration/register.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_username'], password=request.POST['input_password'], email=request.POST['input_email'])
        user.save() 
        messages.success(request, 'Signup Successful!')
        return redirect('login')
       
def view_authenticate_user(request):
    if request.method == "GET":
        return render(request, 'registration/login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_username'], password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request, user)
            return render(request, "registration/home.html")
        else:
            messages.warning(request,'Note: Please chek your username and password!!')
            return redirect('login')

def logout_user(request):
    logout(request)
    messages.warning(request, 'Note: Logout sucessfully!! ')
    return redirect('login')