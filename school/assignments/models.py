from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

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

class Submission(BaseModel):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey("student.Student", on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    file_upload = models.FileField(upload_to='submissions/')

    def do_action(self):
        # Specific submission action
        # For example, you can implement logic to process the submission
        # This method should be customized based on your project's requirements
        pass

    class Meta:
        verbose_name_plural = "Submissions"

    def __str__(self):
        return f"{self.student.full_name()} - {self.assignment.title}"
