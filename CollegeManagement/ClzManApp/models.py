from django.db import models
# Create your models here.

#Result class which stores student names and their result
class Result(models.Model):
    StudentName = models.CharField(max_length=50)
    result=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.StudentName} is {self.result}"   # returns the string when Result object is being called 

#Teachers class which stores the details of the a teacher
class Teachers(models.Model):
    TeacherName=models.CharField(max_length=40)
    email=models.EmailField(max_length=55)
    department=models.CharField(max_length=30)

    def __str__(self):
        return self.TeacherName  #returns TeacherName string when its object is being called

class Class(models.Model):
    ClassName = models.CharField(max_length=128)
    StudentGroupName = models.CharField(max_length=40)
    teachers_class = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='classes') # OneToMany relationship

    def __str__(self):
        return self.ClassName   #returns ClassName string when its object is being called

class Students(models.Model):
    StudentName=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    standard=models.CharField(max_length=50)
    students_result=models.ForeignKey(Result, on_delete=models.CASCADE, related_name='of_students')
    students_class=models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students') 
    # Here ForeignKey specifies one to many relationship between Result, Class classes and Students class

    def __str__(self):
        return self.StudentName     #returns StudentName string when Students class object is being called
    
class Modules(models.Model):
    ModuleName=models.CharField(max_length=30)
    students_modules=models.ManyToManyField(Students, related_name='study_modules')
    teachers_modules=models.ManyToManyField(Teachers,  related_name='teach_modules')
    # Here ManyToManyField specifies Many to Many relationship between modules class and Students, Teachers classes

    def __str__(self):
        return self.ModuleName    #returns ModuleName string when Modules class object is being called

class Attendance(models.Model)
    StudentName = models.CharField(max_length=40)
    ModuleName = models.CharField(max_length=30)
    Attendance = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.StudentName} has {self.Attendance} attendance in {self.ModuleName}"



