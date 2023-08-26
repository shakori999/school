from datetime import date, timedelta
from inspect import walktree
import pytest
from django.contrib.auth.models import User
from ..dashboard.models import Enrollment, Person, Role
from ..student.models import Student
from ..teacher.models import Teacher
from ..course.models import Course

@pytest.fixture
def create_admin_user(django_user_model):
    """
    return admin user
    """

    return django_user_model.objects.create_superuser("admin", "a@a.com", "password")

@pytest.fixture
def user_student():
    return User.objects.create_user(username='testuser',first_name="ali", last_name="mohammed", password='testpass')

@pytest.fixture
def user_teacher():
    return User.objects.create_user(username='teacher',first_name="ali", last_name="mohammed", password='testpass')


@pytest.fixture
def create_student_role():
    role = Role.objects.create(role_name="student")
    return role

@pytest.fixture
def create_teacher_role():
    role = Role.objects.create(role_name="teacher")
    return role

@pytest.fixture
def person_student(user_student, create_student_role):
    person = Person.objects.create(user=user_student,username=user_student.username, role=create_student_role)
    return person

@pytest.fixture
def person_teacher(user_teacher, create_teacher_role):
    person = Person.objects.create(user=user_teacher,username=user_teacher.username, role=create_teacher_role)
    return person

@pytest.fixture
def student(person_student):
    student = Student.objects.create(user=person_student, date_of_birth='2000-01-01', contact_number="123456", address="street" )
    return student


@pytest.fixture
def teacher(person_teacher):
    teacher = Teacher.objects.create(user=person_teacher,subject_taught="math", date_of_birth="1998-01-01", contact_number="1234567", address="ali street")
    return teacher




@pytest.fixture
def course(teacher):
    course = Course.objects.create(name='Mathematics 101', start_date=date.today(), end_date=date.today() + timedelta(days=30), teacher=teacher)
    return course

@pytest.fixture
def enrollment(course,student):
    enrollment = Enrollment.objects.create(student=student, course=course, enrollment_date="2000-01-01")
    return enrollment
