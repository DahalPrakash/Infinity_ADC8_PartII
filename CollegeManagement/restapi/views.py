from django.shortcuts import render
from ClzManApp.models import Students
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

#for updating the database records


@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    if request.method == "GET":
        students = Students.objects.get(id = ID)
        print(type(students.StudentName))
        return JsonResponse({
            "Student Name":students.StudentName,
            "student Email":students.email,
            "Student Standard":students.standard
        })
    
    elif request.method == "PUT":
        print("What's the request =>",request.method)
        stds = Students.objects.get(id=ID)
        print(type(stds.StudentName))

        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))

        stds.StudentName = python_dictionary_object['StudentName']
        stds.email = python_dictionary_object["email"]
        stds.standard = python_dictionary_object["standard"]
        stds.save()
        
        return JsonResponse({
            "Message":"Updated successfully"
        })    
        
    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        })

