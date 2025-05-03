from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewSet, AttendanceViewSet, ExamViewSet

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)
router.register('attendance', AttendanceViewSet)
router.register('exams', ExamViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
