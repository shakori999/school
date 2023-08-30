from django.db import models
from django.core.exceptions import ValidationError

from ..dashboard.models import Person

def validate_phone_number(value):
    if not value.isdigit() or len(value) < 10 or len(value) > 15:
        raise ValidationError("Invalid phone number format")

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    teachername = models.CharField(max_length=100)
    email = models.EmailField()
    phoneno = models.CharField(max_length=20)
    phoneno = models.CharField(max_length=20, validators=[validate_phone_number])
    subject_taught = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.TextField()

    def clean_date_of_birth(self):
        if self.date_of_birth is not None and (self.date_of_birth.year < 1900 or self.date_of_birth.year > 2023):
            raise ValidationError("Invalid date of birth")


    def full_name(self):
        if self.user.user.first_name and self.user.user.last_name != "":
            return f"{self.user.user.first_name} {self.user.user.last_name}"
        else:
            return self.teachername

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name_plural = "Teachers"

class TeachersPerCourse(models.Model):
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    coursespercycle = models.ForeignKey("course.CoursesPerCycle", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Teachers per Course"
        unique_together = ('coursespercycle', 'cycle', 'teacher')

    def __str__(self):
        return f"{self.teacher.full_name()} - {self.coursespercycle.course.name} ({self.cycle.cycledescription})"
