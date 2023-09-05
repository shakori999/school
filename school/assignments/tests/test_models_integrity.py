import pytest

from django.db import IntegrityError

from ..models import Assignment, Submission

@pytest.mark.django_db
def test_empty_description():
    with pytest.raises(IntegrityError):
        Assignment.objects.create(
            title="assignment title",
            description="",  # Empty description
            due_date="2023-01-01",
            description2="disc2",
        )

@pytest.mark.django_db
def test_empty_description2():
    with pytest.raises(IntegrityError):
        Assignment.objects.create(
            title="assignment title",
            description="desic",
            due_date="2023-01-01",
            description2="",  # Empty description2
        )

@pytest.mark.django_db
def test_assignment_without_course():
    with pytest.raises(IntegrityError):
        Assignment.objects.create(
            title="assignment title",
            description="desic",
            due_date="2023-01-01",
            description2="disc2",
        )

@pytest.mark.django_db
def test_long_title():
    with pytest.raises(IntegrityError):
        Assignment.objects.create(
            title="a" * 201,  # Long title exceeding max_length
            description="desic",
            due_date="2023-01-01",
            description2="disc2",
        )



"""
this section for testing submission model
"""

@pytest.mark.django_db
def test_submission_without_assignment(student):
    with pytest.raises(IntegrityError):
        sub = Submission.objects.create(
            student=student,
            submission_date="2023-01-01",
            file_upload="sub.pdf",
        )
        sub.full_clean()
