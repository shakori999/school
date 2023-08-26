from django.contrib.auth.models import User
from django.db import models

from ..dashboard.models import Person

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    subject_taught = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.user.user.first_name} {self.user.user.last_name}"
