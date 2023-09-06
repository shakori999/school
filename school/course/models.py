from django.db import models


from ..dashboard.models import BaseModel
from ..dashboard.enrollment_strategie import *

# Create your models here.
class Course(BaseModel):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE, null=True)
    cycles = models.ManyToManyField('cycle.Cycle', through='CoursesPerCycle')
    description = models.TextField()
    abstract = models.TextField(default="abstract")
    bibliography = models.TextField(default="book")

    class Meta:
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.name

    def get_full_description(self):
        return f"{self.name}: {self.description}\nBibliography: {self.bibliography}"

class CoursesPerCycle(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    coursestartdate = models.DateField()
    courseenddate = models.DateField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(coursestartdate__lte=models.F('courseenddate')),
                                   name='start_before_end')
        ]

    def __str__(self):
        return f"{self.course.name} ({self.cycle.cyclestartdate} - {self.cycle.cycleenddate})"

    #def is_student_enrolled(self, student):
    #    return self.students.filter(id=student.id).exists()

    #def remove_student(self, student):
    #    self.students.remove(student)
