from django.db import models

# Create your models here.
class Result(models.Model):
    ModuleName=models.CharField(max_length=30)
    result=models.CharField(max_length=50)
    StudentID = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.StudentID} is {self.result} in {self.ModuleName}"

class Teachers(models.Model):
    TeacherID=models.CharField(max_length=50)
    TeacherName=models.CharField(max_length=40)
    email=models.EmailField(max_length=55)
    department=models.CharField(max_length=30)

    def __str__(self):
        return self.TeacherName

class Class(models.Model):
    ClassName = models.CharField(max_length=128)
    TeacherID = models.CharField(max_length=50)
    StudentGroupName = models.CharField(max_length=40)
    teacher_class = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return self.ClassName

class Students(models.Model):
    StudentID=models.CharField(max_length=50)
    StudentName=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    standard=models.CharField(max_length=50)
    students_result=models.ForeignKey(Result, on_delete=models.CASCADE, related_name='of_students')
    students_class=models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.StudentName
    

class Modules(models.Model):
    ModuleID=models.CharField(max_length=30)
    ModuleName=models.CharField(max_length=30)
    studentID_modules=models.ManyToManyField(Students, related_name='study_modules')
    teacherID_modules=models.ManyToManyField(Teachers,  related_name='teach_modules')

    def __str__(self):
        return self.ModuleName





