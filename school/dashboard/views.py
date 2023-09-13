from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Person,Role
from .serializers import PersonSerializer,RoleSerializer


class RoleListView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PeronsListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PeronsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Ensure that the associated User object is deleted along with the Person
        if instance.user:
            instance.user.delete()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
