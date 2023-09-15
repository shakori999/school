import pytest
from datetime import time,datetime ,timedelta

from django.utils import timezone
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from ..models import Attendance
from ..serializers import AttendanceSerializer

@pytest.mark.django_db
def test_create_attendance(api_client, course,cycle,student,sample_class):

    # Create an aware datetime for the leave time, ensuring it's after the arrive time
    timearrive = timezone.now().time()
    
    # Assuming sample_class.endtime is a string in "HH:MM" format with ":00" seconds
    endtime_str = sample_class.endtime  # Remove the ":00" part
    
    # Split the endtime_str into hours and minutes
    hours, minutes, second = map(int, endtime_str.split(':'))
    
    # Create a datetime.time object
    endtime = time(hours, minutes)

    # Convert timearrive to a string in "HH:MM:SS" format
    timearrive_str = timearrive.strftime('%H:%M:%S')


    url = reverse('attendance-list')  # Replace with your URL name
    data = {
        "course": course.id,  # Replace with the appropriate course ID
        "cycle": cycle.id,   # Replace with the appropriate cycle ID
        "student": student.id, # Replace with the appropriate student ID
        "class_info": sample_class.id,  # Replace with the appropriate class ID
        "timearrive": timearrive_str ,  # Set arrive time in the future
        "timeleave": endtime,  # Set leave time to the current time
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert Attendance.objects.count() == 1  # Check if a new record is created
    assert Attendance.objects.get(pk=1).timeleave == data["timeleave"]


@pytest.mark.django_db
def test_retrieve_attendance(api_client, attendance):
    attendance = Attendance.objects.first()
    url = reverse('attendance-detail', args=[attendance.id])  # Replace with your URL name
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == AttendanceSerializer(attendance).data


@pytest.mark.django_db
def test_update_attendance(api_client, attendance,course,cycle,student,sample_class):

    # Create an aware datetime for the leave time, ensuring it's after the arrive time
    timearrive = timezone.now().time()

    # Assuming sample_class.endtime is a string in "HH:MM" format with ":00" seconds
    endtime_str = sample_class.endtime  # Remove the ":00" part
    
    # Split the endtime_str into hours and minutes
    hours, minutes, second = map(int, endtime_str.split(':'))
    
    # Create a datetime.time object
    endtime = time(hours, minutes)

    # Convert timearrive to a string in "HH:MM:SS" format
    timearrive_str = timearrive.strftime('%H:%M:%S')


    attendance = Attendance.objects.first()
    url = reverse('attendance-detail', args=[attendance.id])  # Replace with your URL name
    data = {
        "course": course.id,  # Replace with the appropriate course ID
        "cycle": cycle.id,   # Replace with the appropriate cycle ID
        "student": student.id, # Replace with the appropriate student ID
        "class_info": sample_class.id,  # Replace with the appropriate class ID
        "timearrive": timearrive_str ,  # Set arrive time in the future
        "timeleave": endtime,  # Set leave time to the current time
    }
    response = api_client.put(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    attendance.refresh_from_db()
    assert attendance.course_id == 1
    assert attendance.timeleave == data["timeleave"]



@pytest.mark.django_db
def test_delete_attendance(api_client, attendance):
    attendance = Attendance.objects.first()
    url = reverse('attendance-detail', args=[attendance.id])  # Replace with your URL name
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Attendance.objects.count() == 0  # Check if the record has been deleted

