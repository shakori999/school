from django.db import models
from ..dashboard.models import Person 


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['contact_number']),
        ]

    def full_name(self):
        return f"{self.user.user.first_name} {self.user.user.last_name}"

    def __str__(self):
        return self.full_name()
