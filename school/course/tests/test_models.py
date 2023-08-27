import pytest
import datetime

@pytest.mark.django_db
def test_course_creation(course):
    assert str(course) == f"Introduction to Computer Science"

@pytest.mark.django_db
def test_course_per_cycle_creation(course_per_cycle):
    assert str(course_per_cycle) == f"{course_per_cycle.course.name} ({course_per_cycle.cycle.cyclestartdate} - {course_per_cycle.cycle.cycleenddate})"


'''
@pytest.mark.django_db
def test_enroll_student(enrollment, course, student):
    assert not course.is_student_enrolled(student)

    course.enroll_student(student)
    assert enrollment.student == student
    assert enrollment.course == course

    assert course.is_student_enrolled(student)

@pytest.mark.django_db
def test_remove_student(course, student):
    course.enroll_student(student)
    assert course.is_student_enrolled(student)

    course.remove_student(student)

    assert not course.is_student_enrolled(student)

@pytest.mark.django_db
def test_get_enrollment_strategy(course):
    course.enrollment_strategy = 'premium'
    strategy = course.get_enrollment_strategy()

    assert isinstance(strategy, PremiumEnrollmentStrategy)

    course.enrollment_strategy = 'default'
    strategy = course.get_enrollment_strategy()

    assert isinstance(strategy, DefaultEnrollmentStrategy)

@pytest.mark.django_db
def test_str(course):
    assert str(course) == course.name

@pytest.mark.django_db
def test_is_student_enrolled(course, student):
    assert not course.is_student_enrolled(student)

    course.enroll_student(student)

    assert course.is_student_enrolled(student)

@pytest.mark.django_db
def test_enroll_student(course, student):
    # Ensure the student is not already enrolled
    assert not course.students.filter(id=student.id).exists()

    # Enroll the student in the course
    course.enroll_student(student)

    # Verify that the student is now enrolled in the course
    assert course.students.filter(id=student.id).exists()

    # Check if the enrollment details are correct
    enrollment = course.enrollment_set.last()
    assert enrollment.student == student
    assert enrollment.course == course

    # Check if the enrollment date is within the course's start and end dates
    assert course.start_date <= enrollment.created_at.date() <= course.end_date

    # Check if the enrollment strategy is applied correctly
    expected_strategy = course.get_enrollment_strategy().__class__.__name__
    assert enrollment.enrollment_strategy == expected_strategy

    # Cleanup: Delete the student from the course (optional)
    course.students.remove(student)

@pytest.mark.django_db
def test_get_enrollment_strategy(self, course):
    # Set the enrollment strategy to 'premium'
    course.enrollment_strategy = 'premium'
    strategy = course.get_enrollment_strategy()
    assert isinstance(strategy, PremiumEnrollmentStrategy)

    # Set the enrollment strategy to something else
    course.enrollment_strategy = 'default'
    strategy = course.get_enrollment_strategy()
    assert isinstance(strategy, DefaultEnrollmentStrategy)

@pytest.mark.django_db
def test_str_representation(self, course):
    assert str(course) == course.name

@pytest.mark.django_db
def test_verbose_name_plural(self):
    assert Course._meta.verbose_name_plural == 'Classes'
'''
