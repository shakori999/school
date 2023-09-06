import pytest
from datetime import date

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from ..models import Course,CoursesPerCycle


'''
this section for testing coruse model
'''
@pytest.mark.django_db
def test_course_code_max_length():
    # Test name exceeding max length
    max_length = 20
    code = "A" * (max_length + 1)
    with pytest.raises(ValidationError) as e:
        course = Course(code=code, name="Sample Course", description="A description.")
        course.full_clean()
    assert "Ensure this value has at most 20 characters" in str(e.value)

@pytest.mark.django_db
def test_course_name_max_length():
    # Test name exceeding max length
    max_length = 100
    name = "A" * (max_length + 1)
    with pytest.raises(ValidationError) as e:
        course = Course(code="COURSE101", name=name, description="A description.")
        course.full_clean()
    assert "Ensure this value has at most 100 characters" in str(e.value)

@pytest.mark.django_db
def test_course_category_blank():
    # Test null category
    with pytest.raises(ValidationError) as e:
        course = Course(code="COURSE101", name="Sample Course", description="A description.")
        course.full_clean()  # Should not raise any errors

    assert "This field cannot be blank" in str(e.value)

@pytest.mark.django_db
def test_course_description_required():
    # Test missing description
    with pytest.raises(ValidationError) as e:
        course = Course(code="COURSE101", name="Sample Course")
        course.full_clean()
    assert "This field cannot be blank" in str(e.value)


@pytest.mark.django_db
def test_course_abstract_default():
    # Test that a Course instance is created with the default abstract value if not provided
    course = Course(code="COURSE101", name="Sample Course", description="A description.")
    course.save()
    
    assert course.abstract == "abstract"

@pytest.mark.django_db
def test_course_bibliography_default():
    # Test that a Course instance is created with the default bibliography value if not provided
    course = Course(code="COURSE101", name="Sample Course", description="A description.")
    course.save()

    assert course.bibliography == "book"

@pytest.mark.django_db
def test_course_get_full_description():
    # Test the get_full_description method to ensure it returns the expected full description format
    course = Course(code="COURSE101", name="Sample Course", description="A description.")
    course.save()

    full_description = course.get_full_description()
    
    assert "Sample Course: A description" in full_description
    assert "Bibliography: book" in full_description

# Add more tests for the Course model here...


'''
this section for testing corusepercycle model
'''
@pytest.mark.django_db
def test_coursespercyle_course_start_date_before_end_date():
    # Test invalid data: Course start date after end date
    with pytest.raises(ValidationError) as e:
        course = Course(code="COURSE101", name="Sample Course", description="A description.")
        course.save()
        coursespercycle = CoursesPerCycle(
            course=course,
            coursestartdate=date(2023, 9, 1),
            courseenddate=date(2023, 8, 1),
        )
        coursespercycle.full_clean()
    assert "start_before_end" in str(e.value)

@pytest.mark.django_db
def test_courses_per_cycle_start_date_and_end_date_valid(course, cycle):
    # Test valid data: Course start date before course end date
    try:
        CoursesPerCycle.objects.create(
            course=course,
            cycle=cycle,
            coursestartdate="2023-08-31",
            courseenddate="2023-09-01",
        )
    except ValidationError as e:
        # Ensure that no validation error is raised
        pytest.fail(f"Unexpected validation error: {e}")
