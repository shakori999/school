from django.db import models

from ..dashboard.models import Person
from ..course.models import Course

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, through='TeachersPerCourse')
    teachername = models.CharField(max_length=100)
    email = models.EmailField()
    phoneno = models.CharField(max_length=20)
    subject_taught = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.TextField()

    def full_name(self):
        if self.user.user.first_name and self.user.user.last_name != "":
            return f"{self.user.user.first_name} {self.user.user.last_name}"
        else:
            return self.user.user.username

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name_plural = "Teachers"

class TeachersPerCourse(models.Model):
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    teacher = models.ForeignKey("teacher.Teacher", on_delete=models.CASCADE)
    coursespercycle = models.ForeignKey("course.CoursesPerCycle", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Teachers per Course"

    def __str__(self):
        return f"{self.teacher.full_name()} - {self.course.name} ({self.cycle.cycledescription})"
