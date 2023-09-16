import pytest
from datetime import timedelta, datetime

from django.utils import timezone


from ..exames.models import Test, TestsScores

@pytest.fixture
def sample_test(course, cycle,enrollment):
    test =  Test.objects.create(
        course = course,
        cycle = cycle,
        enrollment=enrollment,
        testno = "1",
        testdate = "2023-06-15",
        testtime = "10:23:02",
        agenda = "this is a good test",
    )
    return test

@pytest.fixture
def sample_testscore(course, cycle,student, sample_test):
    testscore =  TestsScores.objects.create(
        course = course,
        cycle = cycle,
        student = student,
        test = sample_test,
        testsno = "2",
        score = "30",
    )
    return testscore


# Create an aware datetime for the leave time, ensuring it's after the arrive time
time = timezone.now().time()
date = timezone.now().date()
# Combine time and date to create a datetime object
datetime_obj = datetime.combine(date, time)

# Convert the datetime object back to time and date
converted_time = datetime_obj.time()
converted_date = datetime_obj.date()

@pytest.fixture
def valid_test_data():
    return {
        "testtime": converted_time.strftime('%H:%M:%S'),
        'testdate': converted_date.strftime('%Y-%m-%d'),
        "testno": 1,
        "agenda": "Valid agenda",
        # Add other required fields here
    }
