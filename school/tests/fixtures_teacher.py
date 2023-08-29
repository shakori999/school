import pytest
from datetime import date
from django.contrib.auth.models import User

from ..teacher.models import Teacher, TeachersPerCourse
from ..dashboard.models import Role, Person


@pytest.fixture
def create_teacher_role():
    role = Role.objects.create(role_name="teacher")
    return role

@pytest.fixture
def user_teacher():
    return User.objects.create_user(username='teacher',first_name="ali2", last_name="mohammed2", password='testpass')

@pytest.fixture
def person_teacher(user_teacher, create_teacher_role):
    person = Person.objects.create(user=user_teacher,username=user_teacher.username, role=create_teacher_role)
    return person

@pytest.fixture
def teacher(person_teacher):
    teacher = Teacher.objects.create(
            user=person_teacher,
            teachername="hussain rida",
            email="john@example.com",
            phoneno="1234567890",
            subject_taught="Computer Science",
            date_of_birth=date(1990, 1, 1),
            address="123 Main St",
            )

    return teacher

@pytest.fixture
def teacher_invalid_username(person_teacher):
    teacher = Teacher.objects.create(
            user=person_teacher,
            teachername="",
            email="john@example.com",
            phoneno="1234567890",
            subject_taught="Computer Science",
            date_of_birth=date(1990, 1, 1),
            address="123 Main St",
            )

    return teacher

@pytest.fixture
def teacher_invalid_email(person_teacher):
    teacher = Teacher.objects.create(
            user=person_teacher,
            teachername="hussain rida",
            email="invalid email",
            phoneno="1234567890",
            subject_taught="Computer Science",
            date_of_birth=date(1990, 1, 1),
            address="123 Main St",
            )

    return teacher

@pytest.fixture
def teacher_invalid_phoneno(person_teacher):
    teacher = Teacher(
        user=person_teacher,
        teachername="Valid Name",
        email="john@example.com",
        phoneno="123",  # Invalid phoneno data
        subject_taught="Computer Science",
        date_of_birth=date(1990, 1, 1),
        address="123 Main St",
    )
    return teacher

@pytest.fixture
def teacher_invalid_subject_taught(person_teacher):
    teacher = Teacher(
        user=person_teacher,
        teachername="Valid Name",
        email="john@example.com",
        phoneno="1234567890",
        subject_taught="",  # Invalid subject_taught data
        date_of_birth=date(1990, 1, 1),
        address="123 Main St",
    )
    return teacher

@pytest.fixture
def teacher_invalid_date_of_birth(person_teacher):
    teacher = Teacher(
        user=person_teacher,
        teachername="Valid Name",
        email="john@example.com",
        phoneno="1234567890",
        subject_taught="Computer Science",
        date_of_birth=None,  # Invalid date_of_birth data
        address="123 Main St",
    )
    return teacher

@pytest.fixture
def teacher_invalid_address(person_teacher):
    teacher = Teacher(
        user=person_teacher,
        teachername="Valid Name",
        email="john@example.com",
        phoneno="1234567890",
        subject_taught="Computer Science",
        date_of_birth=date(1990, 1, 1),
        address="",  # Invalid address data
    )
    return teacher

@pytest.fixture
def teachers_per_course(teacher, course_per_cycle, cycle):
    return TeachersPerCourse.objects.create(
        cycle=cycle,
        teacher=teacher,
        coursespercycle=course_per_cycle,
    )
