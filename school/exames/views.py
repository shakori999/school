from rest_framework import generics

from .models import Test, TestsScores
from .serializers import TestSerializer, TestScoresSerializer

class TestListCreateView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestScoresListCreateView(generics.ListCreateAPIView):
    queryset = TestsScores.objects.all()
    serializer_class = TestScoresSerializer

class TestScoresRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestsScores.objects.all()
    serializer_class = TestScoresSerializer
