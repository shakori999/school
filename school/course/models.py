from django.db import models


from ..dashboard.models import BaseModel
from ..dashboard.enrollment_strategie import *


# Create your models here.
class Course(BaseModel):
    start_date = models.DateField()
    end_date = models.DateField()
    teacher = models.ForeignKey("teacher.Teacher", on_delete=models.CASCADE, null=True)
    enrollment_strategy = models.CharField(max_length=50)

    def enroll_student(self, student):
        strategy = self.get_enrollment_strategy()
        strategy.enroll(self, student)

    def get_enrollment_strategy(self):
        if self.enrollment_strategy == 'premium':
            return PremiumEnrollmentStrategy()
        else:
            return DefaultEnrollmentStrategy()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Classes'

    name = models.CharField(max_length=100)
