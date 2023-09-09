from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

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


    def delete(self, *args, **kwargs):
        # Call the User's delete method when deleting the Person
        if self.user:
            self.user.delete()
        super(Student, self).delete(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['phoneno']),
        ]
        verbose_name_plural = "Students"

    def full_name(self):
        if self.user.user.first_name and self.user.user.last_name:
            return f"{self.user.user.first_name} {self.user.user.last_name}"
        return self.user.user.username


    def __str__(self):
        return self.full_name()

@receiver(post_delete, sender=Student)
def post_delete_user(sender, instance, *args, **kwargs):
        instance.user.delete()

class Enrollment(models.Model):
    course_per_cycle = models.ForeignKey("course.CoursesPerCycle", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollmentdate = models.DateField(null=True)
    cancelled = models.BooleanField(default=False)
    cancellationreason = models.TextField()

    class Meta:
        verbose_name_plural = "Enrollments"

    def __str__(self):
        return f"{self.student.full_name()} - {self.course_per_cycle.course.name}"
