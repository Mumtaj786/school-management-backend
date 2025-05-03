from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student, Teacher, Attendance, Exam, Mark
from .serializers import StudentSerializer, TeacherSerializer, AttendanceSerializer, ExamSerializer, MarkSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Mark

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer



@api_view(['GET'])
def student_report(request, student_id):
    student = Student.objects.get(id=student_id)
    marks = Mark.objects.filter(student=student).select_related('exam')
    report_data = [
        {
            "exam": mark.exam.name,
            "subject": mark.exam.subject,
            "date": mark.exam.date,
            "marks_obtained": mark.marks_obtained
        }
        for mark in marks
    ]
    return Response({
        "student": student.name,
        "report": report_data
    })
