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
        errors.append("This field cannot be blank.")

    # Check if the file exists
    if not os.path.isfile(value.path):
        errors.append("File does not exist.")

    # Check the file size (adjust the limit as needed)
    max_file_size = 10 * 1024 * 1024  # 10 MB
    if value.size > max_file_size:
        errors.append(f"File size exceeds the maximum allowed size of {max_file_size} bytes.")

    # Check the file's content type using python-magic
    mime = magic.Magic()
    detected_mime_type = mime.from_buffer(value.read(1024))  # Read the first 1024 bytes to determine the file type

    # Define supported mime types
    supported_mime_types = ['application/pdf']

    if detected_mime_type not in supported_mime_types:
        errors.append("File type not supported. Supported types: pdf")

    # Check the file name length
    max_length = 43  # Set your desired maximum length for file names
    if len(value.name) > max_length:
        errors.append(f"File name exceeds maximum length of {max_length} characters.")

    if errors:
        raise ValidationError(errors)

class Submission(BaseModel):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey("student.Student", on_delete=models.CASCADE)
    submission_date = models.DateTimeField(
        auto_now_add=True,
        validators=[MinValueValidator(limit_value=timezone.now())]
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
