from django.db import models

# Create your models here.
class Attendance(models.Model):
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    student = models.ForeignKey("student.Student", on_delete=models.CASCADE)
    class_info = models.ForeignKey("classes.Class", on_delete=models.CASCADE)
    timearrive = models.DateTimeField()
    timeleave = models.DateTimeField()
