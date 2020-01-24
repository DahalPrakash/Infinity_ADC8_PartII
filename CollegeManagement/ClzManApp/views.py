
# # from django.shortcuts import render
# # from django.views.generic import TemplateView
# # from django.core.files.storage import FileSystemStorage

# # # Create your views here.


# # def upload(request):
# #     if request.method == 'POST':
# #         uploaded_file = request.FILES['doc']
# #         file_object = FileSystemStorage()
# #         file_object.save(uploaded_file.name, uploaded_file)
# #     return render(request,'home.html')



# from django.shortcuts import render,redirect
# from .models import Student
# from django.core.files.storage import FileSystemStorage

# # Create your views here.

# def get_student_section(req):
#     all_student=Student.objects.all()

#     if 'query_student' in req.GET:
#         query_name=req.GET['query_student']
#         all_student=Student.objects.filter(first_name=query_name)
#     context={
#         "students":all_student
#     }
#     return render(req,"perm.html",context)


# def update_student(req,ID):
#     current_student=Student.objects.get(id=ID)
#     all_students=Student.objects.all()

#     context={
#         "students":all_students,
#         "current_student":current_student
#     }

#     return render(req,"perm.html",context=context)



# def post_update_student(req,ID):
#     first_name=req.POST["first_name"]
#     middle_name=req.POST["middle_name"]
#     last_name=req.POST["last_name"]
#     date_of_birth=req.POST["date_of_birth"]
#     age=req.POST["age"]
#     address=req.POST["address"]
#     phone=req.POST["phone"]
#     email=req.POST["email"]

#     profile_img=req.FILES["profile_img"]

#     fs=FileSystemStorage()
#     filename=fs.save(profile_img.name,profile_img)
#     url=fs.url(filename)


#     current_sudent=Student.objects.get(id=ID)

#     current_sudent.first_name=first_name
#     current_sudent.middle_name=middle_name
#     current_sudent.last_name=last_name
#     current_sudent.date_of_birth=date_of_birth
#     current_sudent.age=age
#     current_sudent.address=address
#     current_sudent.phone=phone
#     current_sudent.email=email
#     current_sudent.profile_img=url

#     current_sudent.save()

#     return redirect("home")


# def post_student(req):
    

#     first_name=req.POST["first_name"]
#     middle_name=req.POST["middle_name"]
#     last_name=req.POST["last_name"]
#     date_of_birth=req.POST["date_of_birth"]
#     age=req.POST["age"]
#     address=req.POST["address"]
#     phone=req.POST["phone"]
#     email=req.POST["email"]

#     profile_img=req.FILES["profile_img"]

#     fs=FileSystemStorage()
#     filename=fs.save(profile_img.name,profile_img)
#     url=fs.url(filename)
    
#     new_student=Student(first_name=first_name,
#         middle_name=middle_name,
#         last_name=last_name,
#         date_of_birth=date_of_birth,
#         age=age,
#         address=address,
#         phone=phone,
#         email=email,
#         profile_img=url)
    
#     new_student.save()

#     return redirect("home")
    

# def delete_student(req,ID):
#     current_student=Student.objects.get(id=ID)
#     current_student.delete()
#     return redirect("home")


