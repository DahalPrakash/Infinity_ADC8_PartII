from django.test import TestCase
from .models import Students
from .models import Result
from .models import Teachers
from .models import Class
from .models import Modules

# Create your tests here.

class studentsModdelTestCase(TestCase):
    def test_student_name_blank_check(self):
        student1= Students.objects.create(StudentName="Mahesh", email="mahesh@gmail.com", standard="BIT")
        self.assertTrue(student1.student_name_blank_check())

    def test_student_result_check(self):
        result1= Result.objects.create(ModuleName="OOP", result="pass", StudentName="Mahesh")
        self.assertTrue(result1.student_result_check())

    def test_teacher_name_blank_check(self):
        teacher1= Teachers.objects.create(TeacherName="Raj Shrestha", email="raj@gmail.com", department="BIT")
        self.assertTrue(teacher1.teacher_name_blank_check())

    def test_class_name_blank_check(self):
        class1=Class.objects.create(ClassName="Seminar Room 1", StudentGroupName="ADC8", teacher_class="Raj")
        self.assertTrue(class1.class_name_blank_check())

    def test_module_name_blank_check(self):
        module1=Modules.objects.create(ModuleName="OOP", studentID="NP03A180111", teacherID="HCK02")
        self.assertTrue(module1.module_name_blank_check())
    
