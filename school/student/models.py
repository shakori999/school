from django.db import models
from ..dashboard.models import Person 


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    courses_per_cycle = models.ManyToManyField("course.CoursesPerCycle", through='Enrollment')
    classes = models.ManyToManyField("classes.Class", through='attendance.Attendance')
    studentname = models.CharField(max_length=100)
    email = models.EmailField()
    birthdate = models.DateField()
    phoneno = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['phoneno']),
        ]

    def full_name(self):
        if self.user.user.first_name and self.user.user.last_name != "":
            return f"{self.user.user.first_name} {self.user.user.last_name}"
        else:
            return self.user.user.username

    def __str__(self):
        return self.full_name()

class Enrollment(models.Model):
    course_per_cycle = models.ForeignKey("course.CoursesPerCycle", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollmentdate = models.DateField()
    cancelled = models.BooleanField(default=False)
    cancellationreason = models.TextField()
