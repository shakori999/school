import pytest

from ..bible_study.models import Lesson,LessonPDF

@pytest.fixture
def sample_lesson(sample_class):
    return Lesson.objects.create(
        lesson_number=1,
        lesson_name="Sample Lesson",
        class_info=sample_class,
    )

# Fixture to create a sample LessonPDF
@pytest.fixture
def sample_lesson_pdf(sample_lesson):
    return LessonPDF.objects.create(
        pdf_file="sample.pdf",
        lesson=sample_lesson,
    )
