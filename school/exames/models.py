from django.db import models

# Create your models here.
class Test(models.Model):
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    enrollment = models.ForeignKey("course.CoursesPerCycle", on_delete=models.CASCADE)
    testno = models.IntegerField()
    testdate = models.DateField()
    testtime = models.TimeField()
    agenda = models.TextField()

class TestsScores(models.Model):
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    student = models.ForeignKey("student.Student", on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    testsno = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
