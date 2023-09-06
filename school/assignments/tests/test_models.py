import pytest

'''
this section for testing assignment model
'''
@pytest.mark.django_db
def test_assignment_creation(assignment):
    assert str(assignment) == f"{assignment.title}"

'''
this section for testing submission model
'''
@pytest.mark.django_db
def test_submission_creation(submission):
    assert str(submission) ==f"{submission.student.full_name()} - {submission.assignment.title}" 

