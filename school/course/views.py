from rest_framework import generics

from .models import Course,CoursesPerCycle
from .serializers import CourseSerializer, CoursesPerCycleSerializer 

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()

class CoursesPerCycleListView(generics.ListCreateAPIView):
    queryset = CoursesPerCycle.objects.all()
    serializer_class = CoursesPerCycleSerializer

class CoursesPerCycleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoursesPerCycle.objects.all()
    serializer_class = CourseSerializer
