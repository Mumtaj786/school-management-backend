from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewSet, AttendanceViewSet, ExamViewSet, MarkViewSet, student_report

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)
router.register('attendance', AttendanceViewSet)
router.register('exams', ExamViewSet)
router.register('marks', MarkViewSet)
path('report/<int:student_id>/', student_report),



urlpatterns = [
    path('', include(router.urls)),
]
