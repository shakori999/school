from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import post_delete

from ..dashboard.models import Person, Role

def validate_phone_number(value):
    if not value.isdigit() or len(value) < 10 or len(value) > 15:
        raise ValidationError("Invalid phone number format")

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    teachername = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, default="teacherpass123")  # Add the password field
    phoneno = models.CharField(max_length=20, validators=[validate_phone_number],unique=True)
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

    def save(self, *args, **kwargs):
        # Create a Person instance
        person = Person.objects.create(
            username=self.teachername,  # Customize as needed
            email=self.email,        # Customize as needed
            password_hash=self.password,
            role=Role.objects.get(role_name='teacher'),  # Customize role lookup
        )

        # Create a User instance
        user = User.objects.create_user(
            username=self.teachername,  # Customize as needed
            password=self.password,  # Customize as needed
            email=self.email,        # Customize as needed
        )

        # Link the User instance to the Person instance
        person.user = user
        person.save()
        self.user = person

        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name_plural = "Teachers"

@receiver(post_delete, sender=Teacher)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()

class TeachersPerCourse(models.Model):
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    coursespercycle = models.ForeignKey("course.CoursesPerCycle", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Teachers per Course"
        unique_together = ('coursespercycle', 'cycle', 'teacher')

    def __str__(self):
        return f"{self.teacher.full_name()} - {self.coursespercycle.course.name} ({self.cycle.cycledescription})"
