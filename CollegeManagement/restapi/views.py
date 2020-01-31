from django.shortcuts import render
from ClzManApp.models import Students
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

#for updating the database records

@csrf_exempt
def view_studentdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_StudentName = request.POST['student_StudentName']
        get_email = request.POST['student_email']
        print(get_StudentID)
        get_standard = request.POST['student_standard']
        print(type(get_StudentID))
        student_obj = Students(StudentID=get_StudentID,StudentName=get_StudentName,email=get_email,standard=get_standard)
        student_obj.save()
        return HttpResponse("<H1>Record Saved</H1>")
    else:
        return HttpResponse("Error record saving")

@csrf_exempt
def view_student_lists(request):
    list_of_students= Students.objects.all()
    print(list_of_students)
    context_variable = {
        'students':list_of_students
    }
    return render(request,'student/student.html',context_variable)

@csrf_exempt
def view_studentdata_updateform(request, ID):
    print(ID)
    student_obj = Students.objects.get(id=ID)
    print(student_obj)
    context_varible = {
        'student':student_obj
    }
    return render(request,'student/studentupdateform.html',context_varible)

@csrf_exempt
def view_update_form_data_in_db(request, ID):
    student_obj = Students.objects.get(id=ID)
    print(student_obj)
    student_form_data = request.POST
    print(student_form_data)
    student_obj.StudentName =request.POST['student_StudentName']
    student_obj.email = request.POST['student_email']
    student_obj.standard = request.POST['student_standard']
    student_obj.save()

    return HttpResponse("<H1>Record Updated!!</H1>")

@csrf_exempt
def view_updateByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        stds = Students.objects.get(id = ID)
        print(type(stds.StudentName))
        return JsonResponse({
            "Student Name":stds.StudentName,
            "Student Email":stds.email,
            "Student Standard":stds.standard
        })
    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        })