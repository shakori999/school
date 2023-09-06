from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class Class(models.Model):
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    coursespercycle = models.ForeignKey("course.CoursesPerCycle", on_delete=models.CASCADE)
    classno = models.IntegerField()
    classtitle = models.CharField(max_length=100, unique=True)
    classdate = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    students = models.ManyToManyField('student.Student', through='attendance.Attendance')

    class Meta:
        ordering = ['classdate', 'starttime']

    def __str__(self):
        return f"{self.classtitle} ({self.classdate} - {self.starttime} to {self.endtime})"

    def validate_time(self):
        if self.starttime >= self.endtime:
            print("Start time must be before end time")
            raise ValidationError("Start time must be before end time")
        if self.classdate < timezone.now().date():
            print("class date cannot be in the past")
            raise ValidationError("Class date cannot be in the past")

    def validate_classno(self):
        if self.classno < 0:
            raise ValidationError("Class number must be greater than or equal to 0")

    def save(self, *args, **kwargs):
        self.validate_time()
        self.validate_classno()
        super().save(*args, **kwargs)
