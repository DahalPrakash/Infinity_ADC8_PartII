from django.db import models

# Create your models here.
class Result(models.Model):
    StudentName = models.CharField(max_length=50)
    result=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.StudentName} is {self.result}"   # returns the string when Result object is being called 

    #For testing
    def student_result_check(self):
        if self.result == " ":
            return False
        else :
            return True


#Teachers class which stores the details of the a teacher
class Teachers(models.Model):
    TeacherName=models.CharField(max_length=40)
    email=models.EmailField(max_length=55)
    department=models.CharField(max_length=30)

    def __str__(self):
        return self.TeacherName  #returns TeacherName string when its object is being called

    #testing for teachers
    def teacher_name_blank_check(self):
        if self.TeacherName == " ":
            return True
        else :
            return False


class Class(models.Model):
    ClassName = models.CharField(max_length=128)
    StudentGroupName = models.CharField(max_length=40)
    
    def __str__(self):
        return self.ClassName   #returns ClassName string when its object is being called

    #testing for Class
    def class_name_blank_check(self):
        classcount = Class.objects.all().count()
        return classcount


class Students(models.Model):
    StudentName=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    standard=models.CharField(max_length=50)

    def __str__(self):
        return self.StudentName     #returns StudentName string when Students class object is being called

    #testing for students
    def student_name_blank_check(self):
        studentcount = Students.objects.all().count()
        return studentcount
    

class Modules(models.Model):
    ModuleName=models.CharField(max_length=30)

    def __str__(self):
        return self.ModuleName    #returns ModuleName string when Modules class object is being called

    #testing for Modules
    def module_name_blank_check(self):
        if self.ModuleName== " ":
            return False
        else :
            return True

class Attendance(models.Model):
    StudentName = models.CharField(max_length=40)
    ModuleName = models.CharField(max_length=30)
    Attendance = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.StudentName} has {self.Attendance} attendance in {self.ModuleName}"


#for pdf upload download

class Book(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to="routine/PDF/")
    
    def __str__(self):
        return self.title

