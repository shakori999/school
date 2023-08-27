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

    class Meta:
        ordering = ['classdate', 'starttime']

    def __str__(self):
        return f"{self.classtitle} ({self.classdate} - {self.starttime} to {self.endtime})"

    def validate_time(self):
        if self.starttime >= self.endtime:
            raise models.ValidationError("Start time must be before end time")

    def save(self, *args, **kwargs):
        self.validate_time()
        super().save(*args, **kwargs)
