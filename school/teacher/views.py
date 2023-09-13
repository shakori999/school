from rest_framework import generics

from .models import Teacher,TeachersPerCourse
from .serializers import TeacherSerializer,TeachersPerCourseSerializer

class TeacherListView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeachersPerCourseListView(generics.ListCreateAPIView):
    queryset = TeachersPerCourse.objects.all()
    serializer_class = TeachersPerCourseSerializer

class TeachersPerCourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeachersPerCourse.objects.all()
    serializer_class = TeachersPerCourseSerializer
