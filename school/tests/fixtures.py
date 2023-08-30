import pytest
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
