import datetime
import pytest

from django.utils import timezone
from django.contrib.auth.models import User

from ..dashboard.models import Role, Person
from ..student.models import Enrollment, Student

@pytest.fixture
def user_student():
    student =  User.objects.create_user(username='testuser',first_name="ali", last_name="mohammed", password='testpass')

    return student

@pytest.fixture
def create_student_role():
    role = Role.objects.create(role_name="student")

    return role

@pytest.fixture
def person_student(user_student, create_student_role):
    person = Person.objects.create(user=user_student,username=user_student.username, role=create_student_role)
    return person


@pytest.fixture
def student(course_per_cycle,person_student):
    student = Student.objects.create(
            user=person_student,
            studentname= "dsf",
            email = "dsf",
            password="studentpass123",
            birthdate = "2000-01-01",
            phoneno = "123456",
            address = "street",
            )
    student.courses_per_cycle.add(course_per_cycle)  # Use .add() to assign a value to many-to-many field
    #student.classes.add(sample_class)  # Use .add() to assign a value to many-to-many field
    return student


@pytest.fixture
def enrollment(student, course_per_cycle):
    try:
        enrollment = Enrollment.objects.create(
            course_per_cycle=course_per_cycle,
            student=student,
            enrollmentdate=timezone.now().date(),
            cancelled=False,
            cancellationreason="",
        )
        return enrollment
    except Exception as e:
        print(f"Error creating enrollment: {e}")
        raise
