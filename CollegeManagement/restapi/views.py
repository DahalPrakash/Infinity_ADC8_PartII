from django.shortcuts import render
from ClzManApp.models import Students
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def view_deleteByID(request,ID):
    if request.method == "DELETE":
        print("What's the request =>",request.method)
        std = Students.objects.get(id=ID)
        print(type(std.StudentName))
        std.delete()

        return JsonResponse({
            "Message":"Deleted successfully"
        })    

    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        })
