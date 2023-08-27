from django.db import models

# Create your models here.
class Class(models.Model):
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    coursespercycle = models.ForeignKey("course.CoursesPerCycle", on_delete=models.CASCADE)
    classno = models.IntegerField()
    classtitle = models.CharField(max_length=100)
    classdate = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    students = models.ManyToManyField('student.Student', through='attendance.Attendance')
