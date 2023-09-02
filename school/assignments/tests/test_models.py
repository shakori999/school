import pytest

@pytest.mark.django_db
def test_assignment_creation(assignment):
    assert str(assignment) == f"{assignment.title}"

@pytest.mark.django_db
def test_submission_creation(submission):
    assert str(submission) ==f"{submission.student.full_name()} - {submission.assignment.title}" 

