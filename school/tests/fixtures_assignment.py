import pytest

from ..assignments.models import Assignment , Submission

@pytest.fixture
def assignment(course):
    assignment =  Assignment.objects.create(
            course = course,
            title = "assignment title",
            description = "desic",
            due_date = "2023-01-01",
            description2 = "disc2",
    )
    return assignment

@pytest.fixture
def submission(assignment, student):
    submission =  Submission.objects.create(
            assignment = assignment,
            student = student,
            submission_date = "2023-01-01",
            file_upload = "sub.pdf",
    )
    return submission
