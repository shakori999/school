from django.db import IntegrityError
import pytest
from django.core.exceptions import ValidationError

from ..models import Lesson, LessonPDF

'''
this section for testing Lesson model
'''

@pytest.mark.django_db
def test_lesson_number_positive_integer(sample_lesson):
    assert sample_lesson.lesson_number > 0

@pytest.mark.django_db
def test_lesson_name_not_empty(sample_lesson):
    assert sample_lesson.lesson_name != ""

@pytest.mark.django_db
def test_verse_to_memorize_optional(sample_lesson):
    # Verse to memorize can be blank or null
    sample_lesson.verse_to_memorize = ""
    sample_lesson.save()
    assert sample_lesson.verse_to_memorize == ""

@pytest.mark.django_db
def test_chapters_to_read_optional(sample_lesson):
    # Chapters to read can be blank or null
    sample_lesson.chapters_to_read = ""
    sample_lesson.save()
    assert sample_lesson.chapters_to_read == ""

@pytest.mark.django_db
def test_class_relationship(sample_lesson):
    assert sample_lesson.class_info is not None


@pytest.mark.django_db
def test_negative_lesson_name_blank(sample_class):
    # Lesson name should not be blank
    with pytest.raises(ValidationError):
        lesson = Lesson.objects.create(
            lesson_number=2,
            lesson_name="",
            class_info=sample_class,
        )
        lesson.full_clean()

@pytest.mark.django_db
def test_negative_verse_to_memorize_blank(sample_class):
    # Verse to memorize can be blank or null
    lesson = Lesson.objects.create(
        lesson_number=3,
        lesson_name="Lesson with Blank Verse",
        class_info=sample_class,
    )
    lesson.verse_to_memorize = None
    lesson.save()
    assert lesson.verse_to_memorize is None

@pytest.mark.django_db
def test_negative_chapters_to_read_blank(sample_class):
    # Chapters to read can be blank or null
    lesson = Lesson.objects.create(
        lesson_number=4,
        lesson_name="Lesson with Blank Chapters",
        class_info=sample_class,
    )
    lesson.chapters_to_read = None
    lesson.save()
    assert lesson.chapters_to_read is None

'''
this section for testing LessonPDF model
'''

@pytest.mark.django_db
def test_pdf_file_upload(sample_lesson_pdf):
    assert sample_lesson_pdf.pdf_file is not None

@pytest.mark.django_db
def test_pdf_file_extension(sample_lesson_pdf):
    # Test that only PDF files are accepted
    with pytest.raises(ValidationError):
        sample_lesson_pdf.pdf_file = "sample.txt"
        sample_lesson_pdf.full_clean()

@pytest.mark.django_db
def test_lesson_relationship(sample_lesson, sample_lesson_pdf):
    assert sample_lesson_pdf.lesson == sample_lesson

@pytest.mark.django_db
def test_negative_pdf_file_upload(sample_lesson):
    # PDF file field should not be empty
    with pytest.raises(ValidationError):
        lesson = LessonPDF.objects.create(
            pdf_file="",
            lesson=sample_lesson,
        )
        lesson.full_clean()

@pytest.mark.django_db
def test_negative_pdf_file_extension(sample_lesson):
    # Test that only PDF files are accepted
    with pytest.raises(ValidationError):
        lesson = LessonPDF.objects.create(
            pdf_file="sample.txt",
            lesson=sample_lesson,
        )
        lesson.full_clean()

@pytest.mark.django_db
def test_uniqueness(sample_lesson, sample_lesson_pdf):
    # Depending on your requirements, you can test uniqueness here
    # For example, you can check that each lesson has only one associated PDF, and vice versa.
    # You may need to customize this based on your specific business logic.
    pass

