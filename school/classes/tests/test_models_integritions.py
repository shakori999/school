import pytest 
from datetime import time

from django.utils import timezone
from django.db import IntegrityError, transaction

from ..models import Class

'''
this section for testing class model
'''
@pytest.mark.django_db
def test_unique_class_title(course, cycle, course_per_cycle):
    # Test invalid data: Duplicate class title
    timenow = timezone.now().date()
    valid_class = Class(
        course=course,
        cycle=cycle,
        coursespercycle=course_per_cycle,
        classno=1,
        classtitle="Sample Class",
        classdate=timenow,
        starttime=time(9, 0, 0),
        endtime=time(11, 0, 0),
    )
    valid_class.save()

    with pytest.raises(IntegrityError) as e:
        with transaction.atomic():
            invalid_class = Class(
                course=course,
                cycle=cycle,
                coursespercycle=course_per_cycle,
                classno=2,
                classtitle="Sample Class",
                classdate=timenow,
                starttime=time(10, 0, 0),
                endtime=time(12, 0, 0),
            )
            invalid_class.save()

    # Ensure that the IntegrityError is raised
    assert isinstance(e.value, IntegrityError)
