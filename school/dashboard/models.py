from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.role_name

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True



def notify_students(sender, instance, **kwargs):
    # Notify students about the new assignment
    pass

post_save.connect(notify_students, sender="assignments.Assignment")


class Person(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=100, unique=True, db_index=True)
    password_hash = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

#class EnrollmentStrategy:
 #   def enroll(self, course, student):
        pass

#class DefaultEnrollmentStrategy(EnrollmentStrategy):
    #def enroll(self, course, student):
        Enrollment.objects.create(course=course, student=student)

#class PremiumEnrollmentStrategy(EnrollmentStrategy):
    #def enroll(self, course, student):
     #   Enrollment.objects.create(course=course, student=student, premium=True)
