import datetime
import pytest
from django.contrib.auth.models import User
from ..dashboard.models import Person, Role
from ..student.models import Enrollment, Student
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
    student =  User.objects.create_user(username='testuser',first_name="ali", last_name="mohammed", password='testpass')
    return student

    #yield student
    #student.delete()

@pytest.fixture
def create_student_role():
    role = Role.objects.create(role_name="student")

    return role
    yield role
    role.delete()

@pytest.fixture
def person_student(user_student, create_student_role):
    person = Person.objects.create(user=user_student,username=user_student.username, role=create_student_role)
    return person
    #yield person
    #person.delete()

@pytest.fixture
def cycle():
    cycle =  Cycle.objects.create(
        cycledescription="Sample Cycle",
        cyclestartdate="2023-01-01",
        cycleenddate="2023-12-31",
        vacationstartdate="2023-06-01",
        vacationenddate="2023-06-15",
    )
    return cycle
    #yield cycle
    #cycle.delete()


@pytest.fixture
def category():
    category = Category.objects.create(
        name="Sample Category",
        categorydescription="Sample Category Description",
    )
    return category
    #yield category
    #category.delete()



@pytest.fixture
def course(category):
    course =  Course.objects.create(
        code="CS101",
        name="Introduction to Computer Science",
        category=category,
        description="This is a sample course description.",
    )
    return course
    #yield course
    #course.delete()

@pytest.fixture
def course_per_cycle(course, cycle):
    cpc =  CoursesPerCycle.objects.create(
        course=course,
        cycle=cycle,
        coursestartdate="2023-01-01",
        courseenddate="2023-12-31",
    )
    return cpc
    #yield cpc 
    #cpc.delete()
    


@pytest.fixture
def sample_class(course, cycle, course_per_cycle):
    class_instance = Class.objects.create(
        course=course,
        cycle=cycle,
        coursespercycle=course_per_cycle,
        classno=1,
        classtitle="Sample Class",
        classdate="2023-09-01",
        starttime="09:00:00",
        endtime="11:00:00",
    )
    return class_instance
    #yield class_instance
    #class_instance.delete()

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
    #yield student
    #student.delete()


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
        #yield enrollment
        #enrollment.delete()
    except Exception as e:
        print(f"Error creating enrollment: {e}")
        raise
    
