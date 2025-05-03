from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    class_name = models.CharField(max_length=50)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=(('Present', 'Present'), ('Absent', 'Absent')))

    class Meta:
        unique_together = ('student', 'date')
class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    subject = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.subject}"

