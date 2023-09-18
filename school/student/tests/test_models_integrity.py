import pytest
from django.utils import timezone
from django.db import IntegrityError
from ..models import Student, Enrollment


'''
this section for testing Student model
'''

@pytest.mark.django_db
def test_student_name_unique(create_student_role):
    # Create a student with a specific studentname
    Student.objects.create(
            studentname="Test Student",
            email="test@example.com",
            birthdate="2000-01-01",
            phoneno="1234567890",
        )
    # Try to create another student with the same studentname, which should raise IntegrityError
    with pytest.raises(IntegrityError):
        Student.objects.create(
                studentname="Test Student",
                email="another@example.com",
                birthdate="2001-01-01",
                phoneno="9876543210"
        )

@pytest.mark.django_db
def test_email_unique(create_student_role):
    # Create a student with a specific email
    Student.objects.create(
            studentname="First Student",
            email="test@example.com",
            birthdate="2000-01-01",
            phoneno="1234567890"
        )
    # Try to create another student with the same email, which should raise IntegrityError
    with pytest.raises(IntegrityError):
        Student.objects.create(
                studentname="Second Student",
                email="test@example.com",
                birthdate="2001-01-01",
                phoneno="9876543210"
        )

@pytest.mark.django_db
def test_phoneno_unique(create_student_role):
    # Create a student with a specific phoneno
    Student.objects.create(
            studentname="Test Student",
            email="test@example.com",
            birthdate="2000-01-01",
            phoneno="1234567890"
        )
    # Try to create another student with the same phoneno, which should raise IntegrityError
    with pytest.raises(IntegrityError):
        Student.objects.create(
                studentname="Another Student",
                email="another@example.com",
                birthdate="2001-01-01",
                phoneno="1234567890"
        )

@pytest.mark.django_db
def test_user_creation(create_student_role):
    # Create a student object
    student = Student(
        studentname="Test Student",
        email="test@example.com",
        birthdate="2000-01-01",
        phoneno="1234567890",
        password="studentpass123",
    )
    student.save()  # This should trigger the creation of corresponding Person and User instances
    assert student.user is not None  # Ensure that the user field is populated

'''
this section for testing Enrollemnt model
'''
@pytest.mark.django_db
def test_course_per_cycle_foreign_key_integrity(student, course_per_cycle):
    # Create an enrollment with a valid student and course_per_cycle
    enrollment = Enrollment.objects.create(
        course_per_cycle=course_per_cycle,
        student=student,
        enrollmentdate=timezone.now().date(),
        cancelled=False,
        cancellationreason="",

    )
    # Retrieve the created enrollment and check its course_per_cycle foreign key
    retrieved_enrollment = Enrollment.objects.get(id=enrollment.id)
    assert retrieved_enrollment.course_per_cycle == course_per_cycle

@pytest.mark.django_db
def test_student_foreign_key_integrity(student,course_per_cycle):
    # Create an enrollment with a valid student and course_per_cycle
    enrollment = Enrollment.objects.create(
        course_per_cycle=course_per_cycle,
        student=student,
        enrollmentdate=timezone.now().date(),
        cancelled=False,
        cancellationreason="",

    )

    # Retrieve the created enrollment and check its student foreign key
    retrieved_enrollment = Enrollment.objects.get(id=enrollment.id)
    assert retrieved_enrollment.student == student

@pytest.mark.django_db
def test_studnet_foreign_key_not_provide_integrity(student, course_per_cycle):
    # Create an enrollment with a valid student and course_per_cycle
    with pytest.raises(IntegrityError):
        enrollment = Enrollment.objects.create(
            course_per_cycle=course_per_cycle,
            enrollmentdate=timezone.now().date(),
            cancelled=False,
            cancellationreason="",

        )
        enrollment.full_clean()

@pytest.mark.django_db
def test_course_per_cycle_foreign_key_not_provide_integrity(student, course_per_cycle):
    # Create an enrollment with a valid student and course_per_cycle
    with pytest.raises(IntegrityError):
        enrollment = Enrollment.objects.create(
            enrollmentdate=timezone.now().date(),
            student=student,
            cancelled=False,
            cancellationreason="",

        )
        enrollment.full_clean()
