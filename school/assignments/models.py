import os
import magic
from django.utils import timezone

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, FileExtensionValidator

from ..dashboard.models import BaseModel

# Create your models here.
class Assignment(BaseModel):
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(validators=[MinValueValidator(limit_value=timezone.now().date())])
    description2 = models.TextField()

    def perform_action(self):
        self.before_action()
        self.do_action()
        self.after_action()

    def before_action(self):
        pass

    def do_action(self):
        raise NotImplementedError("Subclasses must implement the do_action method.")

    def after_action(self):
        pass

    class Meta:
        verbose_name_plural = "Assignments"

    def __str__(self):
        return self.title

def validate_submission_file(value):
    errors = []

    # Check if the not blank
    if not value:
        raise ValidationError("This field cannot be blank.")

    # Check the file size (adjust the limit as needed)
    max_file_size = 10 * 1024 * 1024  # 10 MB
    if value.size > max_file_size:
        raise ValidationError(f"File size exceeds the maximum allowed size of {max_file_size} bytes.")

    # Here's an example of how to check the file extension:
    allowed_extensions = ['.pdf', '.doc', '.docx']
    file_name = value.name
    if not file_name.lower().endswith(tuple(allowed_extensions)):
        raise ValidationError(f"Unsupported file format. Supported formats: {', '.join(allowed_extensions)}")

    # Check the file name length
    max_length = 50  # Set your desired maximum length for file names
    if len(value.name) > max_length:
        raise ValidationError(f"File name exceeds maximum length of {max_length} characters.")

    return value


class Submission(BaseModel):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey("student.Student", on_delete=models.CASCADE)
    submission_date = models.DateTimeField(
        auto_now_add=True,
        validators=[MinValueValidator(limit_value=timezone.now().replace(second=0, microsecond=0))]
    )
    file_upload = models.FileField(
        upload_to='submissions/',
        validators=[validate_submission_file]
    )

    def do_action(self):
        # Specific submission action
        # For example, you can implement logic to process the submission
        # This method should be customized based on your project's requirements
        pass


    class Meta:
        verbose_name_plural = "Submissions"

    def __str__(self):
        return f"{self.student.full_name()} - {self.assignment.title}"
