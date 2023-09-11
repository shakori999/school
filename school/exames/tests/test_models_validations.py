import pytest
from datetime import timedelta

from django.core.exceptions import ValidationError
from django.utils import timezone

from ..models import Test,TestsScores

'''
this section for testing Test model
'''

@pytest.mark.django_db
def test_test_date_not_in_past(valid_test_data):
    valid_test_data["testdate"] = timezone.now().date() - timedelta(days=1)
    with pytest.raises(ValidationError):
        Test(**valid_test_data).full_clean()

@pytest.mark.django_db
def test_test_number_positive_integer(valid_test_data):
    valid_test_data["testno"] = 0
    with pytest.raises(ValidationError):
        Test(**valid_test_data).full_clean()

@pytest.mark.django_db
def test_test_agenda_max_length(valid_test_data):
    valid_test_data["agenda"] = "A" * (Test._meta.get_field("agenda").max_length + 1)
    with pytest.raises(ValidationError):
        Test(**valid_test_data).full_clean()

@pytest.mark.django_db
def test_required_agenda_are_provided(course,cycle,enrollment):
    test = Test(
        course=course,
        cycle=cycle,
        enrollment=enrollment,
        testno=1,
        testdate="2023-09-15",
        testtime="10:30",
    )
    with pytest.raises(ValidationError):
        test.full_clean()

@pytest.mark.django_db
def test_required_testtime_are_provided(course,cycle,enrollment):
    test = Test(
        course=course,
        cycle=cycle,
        enrollment=enrollment,
        testno=1,
        testdate="2023-09-15",
        agenda="Valid agenda",
    )
    with pytest.raises(ValidationError):
        test.full_clean()

@pytest.mark.django_db
def test_required_testdate_are_provided(course,cycle,enrollment):
    test = Test(
        course=course,
        cycle=cycle,
        enrollment=enrollment,
        testno=1,
        testdate="2023-09-1",
        testtime="10:30",
        agenda="Valid agenda",
    )
    with pytest.raises(ValidationError):
        test.full_clean()

@pytest.mark.django_db
def test_required_testno_are_provided(course,cycle,enrollment):
    test = Test(
        course=course,
        cycle=cycle,
        enrollment=enrollment,
        testdate="2023-09-15",
        testtime="10:30",
        agenda="Valid agenda",
    )
    with pytest.raises(ValidationError):
        test.full_clean()

@pytest.mark.django_db
def test_required_enrollment_are_provided(course,cycle):
    test = Test(
        course=course,
        cycle=cycle,
        testno=1,
        testdate="2023-09-15",
        testtime="10:30",
        agenda="Valid agenda",
    )
    with pytest.raises(ValidationError):
        test.full_clean()

@pytest.mark.django_db
def test_required_cycle_are_provided(course,enrollment):
    test = Test(
        course=course,
        enrollment=enrollment,
        testno=1,
        testdate="2023-09-15",
        testtime="10:30",
        agenda="Valid agenda",
    )
    with pytest.raises(ValidationError):
        test.full_clean()

@pytest.mark.django_db
def test_required_course_are_provided(cycle,enrollment):
    test = Test(
        cycle=cycle,
        enrollment=enrollment,
        testno=1,
        testdate="2023-09-15",
        testtime="10:30",
        agenda="Valid agenda",
    )
    with pytest.raises(ValidationError):
        test.full_clean()

@pytest.mark.django_db
def test_valid_foreign_keys(valid_test_data,course,cycle,enrollment):
    # Create related objects (Course, Cycle, Enrollment) as needed
    # Replace the following lines with actual object creation
    valid_test_data["course"] = course
    valid_test_data["cycle"] = cycle
    valid_test_data["enrollment"] = enrollment

    Test(**valid_test_data).full_clean()

'''
this section for testing TestScores model
'''

@pytest.mark.django_db
def test_valid_score():
    # Test a valid score within the range [0, 100]
    valid_score = TestsScores(
        score=50.0
    )
    valid_score.clean()

@pytest.mark.django_db
def test_score_below_minimum():
    # Test a score below the minimum (less than 0)
    with pytest.raises(ValidationError, match="Score must be between 0 and 100"):
        invalid_score = TestsScores(
            score=-1.0  # An invalid score below 0
        )
        invalid_score.clean()

@pytest.mark.django_db
def test_score_above_maximum():
    # Test a score above the maximum (greater than 100)
    with pytest.raises(ValidationError, match="Score must be between 0 and 100"):
        invalid_score = TestsScores(
            score=101.0  # An invalid score above 100
        )
        invalid_score.clean()

@pytest.mark.django_db
def test_positive_testsno():
    # Test a valid positive integer for testsno
    valid_testsno = TestsScores(
        score=1,
        testsno=1,
    )
    valid_testsno.clean()

@pytest.mark.django_db
def test_non_positive_testsno():
    # Test a non-positive value for testsno
    with pytest.raises(ValidationError, match="Ensure this value is greater than or equal to 1"):
        invalid_testsno = TestsScores(
            score=1,
            testsno=0  # An invalid non-positive value for testsno
        )
        invalid_testsno.full_clean()
