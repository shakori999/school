import pytest

from django.db import IntegrityError

from ..models import Lesson,LessonPDF

'''
this section for testing Lesson model
'''

@pytest.mark.django_db
def test_negative_lesson_number(sample_class):
    # Lesson number should not be negative
    with pytest.raises(IntegrityError):
        Lesson.objects.create(
            lesson_number=-1,
            lesson_name="Negative Lesson",
            class_info=sample_class,
        )

@pytest.mark.django_db
def test_negative_class_relationship():
    # Lesson should be associated with a valid class
    with pytest.raises(IntegrityError):
        lesson = Lesson.objects.create(
            lesson_number=5,
            lesson_name="Lesson with Invalid Class",
            class_info=None,  # Invalid class relationship
        )
        lesson.full_clean()


'''
this section for testing LessonPDF model
'''

@pytest.mark.django_db
def test_negative_lesson_relationship():
    # LessonPDF should be associated with a valid lesson
    with pytest.raises(IntegrityError):
        lesson = LessonPDF.objects.create(
            pdf_file="sample.pdf",
            lesson=None,  # Invalid lesson relationship
        )
        lesson.full_clean()
