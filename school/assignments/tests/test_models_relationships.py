import pytest

from ..models import Assignment, Submission

'''
this section for testing assignment model
'''
@pytest.mark.django_db
def test_assignment_relationship(assignment, course):
    # Create an assignment instance
    assignment = assignment

    # Retrieve the created Assignment instance from the database
    assignment_from_db = Assignment.objects.get(id=assignment.id)

    # Retrieve the associated course
    associated_course = assignment_from_db.course

    # Perform assertions to check the relationships
    assert associated_course == course
    assert str(assignment_from_db) == assignment.title


'''
this section for testing submission model
'''

@pytest.mark.django_db
def test_submission_relationship(submission, assignment, student):
    # Create a submission instance
    submission = submission

    # Retrieve the created Submission instance from the database
    submission_from_db = Submission.objects.get(id=submission.id)

    # Retrieve the associated assignment and student
    associated_assignment = submission_from_db.assignment
    associated_student = submission_from_db.student

    # Perform assertions to check the relationships
    assert associated_assignment == assignment
    assert associated_student == student
    assert str(submission_from_db) == f"{student.full_name()} - {assignment.title}"

