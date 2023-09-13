from rest_framework import generics
from .models import Class
from .serializers import ClassSerializer

class ClassListView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ClassDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
