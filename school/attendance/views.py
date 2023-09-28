from rest_framework import generics, status
from rest_framework.response import Response

from datetime import datetime, timedelta
from django.utils import timezone
from .models import Attendance
from .serializers import AttendanceSerializer
from ..classes.models import Class

class AttendanceListView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        # Create a mutable copy of the request data
        data = request.data.copy()
        
        # Automatically set the timearrive field to the current time
        data['timearrive'] = timezone.now().time()

        class_info_id = data.get('class_info')
        if class_info_id is not None:
            class_info = Class.objects.get(pk=class_info_id)
            # Automatically set the timeleave field based on class_endtime
            data['timeleave'] = class_info.endtime


        # Get the class start datetime as an offset-aware datetime
        class_start_datetime = timezone.make_aware(datetime.combine(class_info.classdate, class_info.starttime))

        # Get the current datetime as an offset-aware datetime
        current_datetime = timezone.now()

        # Calculate the time difference
        time_difference = class_start_datetime - current_datetime

        # Check if the student is arriving more than 5 minutes before class start
        if time_difference > timedelta(minutes=5):
            return Response({"error": "Student cannot mark attendance more than 5 minutes before class start."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
