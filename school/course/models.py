from django.db import models


from ..dashboard.models import BaseModel
from ..dashboard.enrollment_strategie import *

# Create your models here.
class Course(BaseModel):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE, null=True)
    cycles = models.ManyToManyField('cycle.Cycle', through='CoursesPerCycle')
    teachers = models.ManyToManyField('teacher.Teacher', through='teacher.TeachersPerCourse')
    description = models.TextField()
    abstract = models.TextField(default="abstract")
    bibliography = models.TextField(default="book")

class CoursesPerCycle(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    coursestartdate = models.DateField()
    courseenddate = models.DateField()

    #students = models.ManyToManyField("student.Student", related_name='courses_enrolled', blank=True)
    #enrollment_strategy = models.CharField(max_length=50)


    #def get_enrollment_strategy(self):
    #    if self.enrollment_strategy == 'premium':
    #        return PremiumEnrollmentStrategy()
    #    else:
    #        return DefaultEnrollmentStrategy()

    #def enroll_student(self, student):
    #    strategy = self.get_enrollment_strategy()
    #    strategy.enroll(self, student)
    #    self.save()


    #def is_student_enrolled(self, student):
    #    return self.students.filter(id=student.id).exists()

    #def remove_student(self, student):
    #    self.students.remove(student)

    #def __str__(self):
    #    return self.name

    #class Meta:
    #    verbose_name_plural = 'Classes'


