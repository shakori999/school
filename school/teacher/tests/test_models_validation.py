import pytest
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from ...teacher.models import TeachersPerCourse

@pytest.mark.django_db
def test_teacher_invalid_username(teacher_invalid_username):
    with pytest.raises(ValidationError) as e:
        teacher_invalid_username.full_clean()
    
    assert "teachername" in e.value.message_dict

@pytest.mark.django_db
def test_teacher_invalid_email(teacher_invalid_email):
    with pytest.raises(ValidationError) as e:
        teacher_invalid_email.full_clean()
    
    assert "email" in e.value.message_dict

@pytest.mark.django_db
def test_teacher_invalid_phoneno(teacher_invalid_phoneno):
    with pytest.raises(ValidationError) as e:
        teacher_invalid_phoneno.full_clean()

    assert "phoneno" in e.value.message_dict

@pytest.mark.django_db
def test_teacher_invalid_subject_taught(teacher_invalid_subject_taught):
    with pytest.raises(ValidationError) as e:
        teacher_invalid_subject_taught.full_clean()

    assert "subject_taught" in e.value.message_dict


@pytest.mark.django_db
def test_teacher_invalid_address(teacher_invalid_address):
    with pytest.raises(ValidationError) as e:
        teacher_invalid_address.full_clean()

    assert "address" in e.value.message_dict

@pytest.mark.django_db
def test_teacher_invalid_date_format(teacher_invalid_date_of_birth):
    invalid_dates = [
        "invalid_date", #not a date
        "22023-08-30",  # Invalid year and day
        "2023-08-32",  # Invalid  day
        "2023-13-15",  # Invalid month
        "2023-02-30",  # February cannot have 30th day
    ]

    for date_str in invalid_dates:
        with pytest.raises(ValidationError) as e:
            teacher_invalid_date_of_birth.date_of_birth=date_str
            teacher_invalid_date_of_birth.full_clean()


        assert "date_of_birth" in e.value.error_dict



"""
this section for testing teacherpercourse model
"""

@pytest.mark.django_db
def test_teachers_per_course_missing_cycles(teacher, course_per_cycle):
    with pytest.raises(IntegrityError):
        TeachersPerCourse.objects.create(
            cycle=None,
            teacher=teacher,
            coursespercycle=course_per_cycle,
        )

@pytest.mark.django_db
def test_teachers_per_course_missing_teacher(cycle, course_per_cycle):
    with pytest.raises(IntegrityError):
        TeachersPerCourse.objects.create(
            cycle=cycle,
            teacher=None,
            coursespercycle=course_per_cycle,
        )

@pytest.mark.django_db
def test_teachers_per_course_missing_coursepercycle(cycle,teacher):
    with pytest.raises(IntegrityError):
        TeachersPerCourse.objects.create(
            cycle=cycle,
            teacher=teacher,
            coursespercycle=None,
        )
