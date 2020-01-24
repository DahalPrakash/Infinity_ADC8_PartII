# from django.db import models

# # Create your models here.

# class Image(models.Model):
#     name= models.CharField(max_length=500)
#     videofile= models.FileField(upload_to='images/', null=True, verbose_name="")

# def __str__(self):
#     return self.name + ": " + str(self.imagefile)


from django.db import models

# Create your models here.
# class Event(models.Model):
#     event_name = models.CharField('Event Name',max_length=100)
#     venue = models.CharField('Venue',max_length=100)
#     event_date = models.DateTimeField('Event Date')
#     manager = models.CharField('Manager Name', max_length=100)
#     event_description=models.CharField('Event Description',max_length=200) 

class Student(models.Model):
    Student_name=models.CharField(max_length=30)
    email=models.CharField(max_length=20)
    standard=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Student_name

class Result(models.Model):
    ModuleName=models.CharField(max_length=30)
    result=models.CharField(max_length=30)
    Student_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Student_name + self.ModuleName + self.result
     

class Teacher(models.Model):
    TeacherName=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    department=models.CharField(max_length=40)

    def __str__(self):
        return self.TeacherName
