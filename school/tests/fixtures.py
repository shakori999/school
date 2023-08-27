from datetime import date, timedelta
from inspect import walktree
import datetime
import pytest
from django.contrib.auth.models import User
from ..dashboard.models import Person, Role
from ..student.models import Enrollment, Student
from ..teacher.models import Teacher, TeachersPerCourse
from ..course.models import Course, CoursesPerCycle
from ..cycle.models import Cycle
from ..categories.models import Category
from ..classes.models import Class

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
    return User.objects.create_user(username='teacher',first_name="ali2", last_name="mohammed2", password='testpass')


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
def cycle():
    return Cycle.objects.create(
        cycledescription="Sample Cycle",
        cyclestartdate="2023-01-01",
        cycleenddate="2023-12-31",
        vacationstartdate="2023-06-01",
        vacationenddate="2023-06-15",
    )

@pytest.fixture
def category():
    return Category.objects.create(
        name="Sample Category",
        categorydescription="Sample Category Description",
    )


@pytest.fixture
def course(category):
    return Course.objects.create(
        code="CS101",
        name="Introduction to Computer Science",
        category=category,
        description="This is a sample course description.",
    )
@pytest.fixture
def course_per_cycle(course, cycle):
    return CoursesPerCycle.objects.create(
        course=course,
        cycle=cycle,
        coursestartdate="2023-01-01",
        courseenddate="2023-12-31",
    )
@pytest.fixture
def sample_class(course, cycle, course_per_cycle):
    return Class.objects.create(
        course=course,
        cycle=cycle,
        coursespercycle=course_per_cycle,
        classno=1,
        classtitle="Sample Class",
        classdate="2023-09-01",
        starttime="09:00:00",
        endtime="11:00:00",
    )

@pytest.fixture
def student(person_student, course_per_cycle):
    student = Student.objects.create(
            user=person_student,
            studentname= "dsf",
            email = "dsf",
            birthdate = "2000-01-01",
            phoneno = "123456",
            address = "street",
            )
    student.courses_per_cycle.add(course_per_cycle)  # Use .add() to assign a value to many-to-many field
    return student


@pytest.fixture
def enrollment(student, course_per_cycle):
    try:
        enrollment = Enrollment.objects.create(
            course_per_cycle=course_per_cycle,
            student=student,
            enrollmentdate=datetime.date(2023, 1, 1),
            cancelled=False,
            cancellationreason="",
        )
        return enrollment
    except Exception as e:
        print(f"Error creating enrollment: {e}")
        raise

@pytest.fixture
def teacher(person_teacher):
    teacher = Teacher.objects.create(
            user=person_teacher,
            teachername="John Doe",
            email="john@example.com",
            phoneno="1234567890",
            subject_taught="Computer Science",
            date_of_birth=date(1990, 1, 1),
            address="123 Main St",
            )

    return teacher


@pytest.fixture
def teachers_per_course(teacher, course_per_cycle, cycle):
    return TeachersPerCourse.objects.create(
        cycle=cycle,
        teacher=teacher,
        coursespercycle=course_per_cycle,
    )


