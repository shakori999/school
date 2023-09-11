from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Test(models.Model):
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    enrollment = models.ForeignKey("student.Enrollment", on_delete=models.CASCADE)
    testno = models.IntegerField(validators=[MinValueValidator(1)])
    testdate = models.DateField()
    testtime = models.TimeField()
    agenda = models.TextField(max_length=200)


    class Meta:
        verbose_name_plural = "Tests"

    def clean(self):
        if self.testdate < timezone.now().date():
            raise ValidationError("Test date cannot be in the past")

    def __str__(self):
        return f"{self.course.name} - Test {self.testno} ({self.testdate} at {self.testtime})"

class TestsScores(models.Model):
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    cycle = models.ForeignKey("cycle.Cycle", on_delete=models.CASCADE)
    student = models.ForeignKey("student.Student", on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    testsno = models.IntegerField(validators=[MinValueValidator(1)])
    score = models.DecimalField(max_digits=5, decimal_places=2, validators=[
        MinValueValidator(0), MaxValueValidator(100)
    ])

    class Meta:
        verbose_name_plural = "Tests Scores"

    def clean(self):
        if self.score < 0 or self.score > 100:
            raise ValidationError("Score must be between 0 and 100")
        
        if self.testsno is not None and self.testsno <= 0:
            raise ValidationError("Ensure this value is greater than or equal to 1")

    def __str__(self):
        return f"{self.student.full_name()} - {self.test.course.name} - Test {self.testsno}: {self.score}"
