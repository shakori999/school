from django.db import models
from django.core.validators import FileExtensionValidator



class Lesson(models.Model):
    class_info = models.ForeignKey("classes.Class", on_delete=models.CASCADE, related_name='lessons')

    # Fields for individual lessons
    lesson_number = models.PositiveIntegerField()
    lesson_name = models.CharField(max_length=255)

    # Fields specific to each lesson
    verse_to_memorize = models.CharField(max_length=255, blank=True, null=True)
    chapters_to_read = models.CharField(max_length=255, blank=True, null=True)
    pdf_file = models.FileField(upload_to='lesson_pdfs/', blank=True, null=True)

    # Add other fields related to lessons as needed

    def __str__(self):
        return f"Lesson {self.lesson_number} for {self.class_info}"


class LessonPDF(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name='pdf')
    pdf_file = models.FileField(
        upload_to='lesson_pdfs/', 
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )

    def __str__(self):
        return f"PDF for Lesson {self.lesson.lesson_number}"

    class Meta:
        verbose_name = "Lesson PDF"
        verbose_name_plural = "Lesson PDFs"

