from django.test import TestCase
from ClzManApp.models import *

# Create your tests here.

class studentsModdelTestCase(TestCase):
    def test_student_name_blank_check(self):
        student1= Students.objects.create(StudentName="Mahesh", email="mahesh@gmail.com", standard="BIT")
        self.assertEqual(student1.student_name_blank_check(),1)

    def test_student_result_check(self):
        result1= Result.objects.create(StudentName="Mahesh", result="pass" )
        self.assertTrue(result1.student_result_check())

    def test_teacher_name_blank_check(self):
        teacher1= Teachers.objects.create(TeacherName="Raj Shrestha", email="raj@gmail.com", department="BIT")
        self.assertFalse(teacher1.teacher_name_blank_check())

    def test_class_name_blank_check(self):
        class1=Class.objects.create(ClassName="Seminar Room 1", StudentGroupName="ADC8")
        self.assertNotEqual(class1.class_name_blank_check(),-1)

    def test_module_name_blank_check(self):
        module1=Modules.objects.create(ModuleName="OOP")
        self.assertTrue(module1.module_name_blank_check())
    
