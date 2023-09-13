from rest_framework import generics

from .models import Cycle
from .serializers import CycleSerializer
# Create your views here.
class CycleListView(generics.ListCreateAPIView):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer

class CycleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
