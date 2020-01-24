from django.db import models

# Create your models here.
class Result(models.Model):
    ModuleName=models.CharField(max_length=30)
    result=models.CharField(max_length=50)
    StudentName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.StudentName} is {self.result} in {self.ModuleName}"
    #testing for result
    def student_result_check(self):
        if self.result == " ":
            return False
        else :
            return True

class Teachers(models.Model):
    TeacherName=models.CharField(max_length=40)
    email=models.EmailField(max_length=55)
    department=models.CharField(max_length=30)

    def __str__(self):
        return self.TeacherName
    #testing for result
    def teacher_name_blank_check(self):
        if self.TeacherName == " ":
            return False
        else :
            return True

class Class(models.Model):
    ClassName = models.CharField(max_length=128)
    StudentGroupName = models.CharField(max_length=40)
    teacher_class = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return self.ClassName
    
    #testing for Class
    def class_name_blank_check(self):
        if self.ClassName == " ":
            return False
        else :
            return True

class Students(models.Model):
    StudentName=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    standard=models.CharField(max_length=50)
    students_result=models.ForeignKey(Result, on_delete=models.CASCADE, related_name='of_students')
    students_class=models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.StudentName
    #testing for students
    def student_name_blank_check(self):
        if self.StudentName == " ":
            return False
        else :
            return True


class Modules(models.Model):
    ModuleName=models.CharField(max_length=30)
    studentID_modules=models.ManyToManyField(Students, related_name='study_modules')
    teacherID_modules=models.ManyToManyField(Teachers,  related_name='teach_modules')

    def __str__(self):
        return self.ModuleName
    #testing for Modules
    def module_name_blank_check(self):
        if self.ModuleName== " ":
            return False
        else :
            return True


