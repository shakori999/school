from django.db import models


from django.utils import timezone

from django.core.exceptions import ValidationError

# Create your models here.
class Attendance(models.Model):
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    student = models.ForeignKey("student.Student", on_delete=models.CASCADE)
    class_info = models.ForeignKey("classes.Class", on_delete=models.CASCADE)
    timearrive = models.TimeField(default=timezone.now().time())
    timeleave = models.TimeField()

    class Meta:
        verbose_name_plural = "Attendance"

    def __str__(self):
        return f"{self.student.full_name()} - {self.class_info.classtitle} ({self.class_info.classdate})"

    def validate_time(self):
        if self.timearrive > self.timeleave:
            raise ValidationError("Arrival time must be before leave time")

    def save(self, *args, **kwargs):
        self.validate_time()
        super().save(*args, **kwargs)
