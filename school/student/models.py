from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.core.exceptions import ValidationError
from django.utils import timezone

from ..dashboard.models import Person, Role 


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    courses_per_cycle = models.ManyToManyField("course.CoursesPerCycle", through='Enrollment')
    classes = models.ManyToManyField("classes.Class", through='attendance.Attendance')
    studentname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100, default="studentpass123")  # Add the password field
    birthdate = models.DateField()
    phoneno = models.CharField(max_length=20)
    address = models.TextField()


    class Meta:
        indexes = [
            models.Index(fields=['phoneno']),
        ]
        verbose_name_plural = "Students"

    def full_name(self):
        if self.user.user.first_name and self.user.user.last_name:
            return f"{self.user.user.first_name} {self.user.user.last_name}"
        return self.user.user.username

    def save(self, *args, **kwargs):
        # Create a Person instance
        person = Person.objects.create(
            username=self.studentname,  # Customize as needed
            email=self.email,        # Customize as needed
            password_hash=self.password,
            role=Role.objects.get(role_name='student'),  # Customize role lookup
        )

        # Create a User instance
        user = User.objects.create_user(
            username=self.studentname,  # Customize as needed
            password=self.password,  # Customize as needed
            email=self.email,        # Customize as needed
        )

        # Link the User instance to the Person instance
        person.user = user
        person.save()
        self.user = person

        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name()

@receiver(post_delete, sender=Student)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()

class Enrollment(models.Model):
    course_per_cycle = models.ForeignKey("course.CoursesPerCycle", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollmentdate = models.DateField(null=True)
    cancelled = models.BooleanField(default=False)
    cancellationreason = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Enrollments"

    def clean(self):
        if self.cancelled and not self.cancellationreason:
            raise ValidationError("Cancellation reason is required for canceled enrollments")

        if self.enrollmentdate and self.enrollmentdate < timezone.now().date():
            raise ValidationError("Enrollment date cannot be in the past")


    def __str__(self):
        return f"{self.student.full_name()} - {self.course_per_cycle.course.name}"
