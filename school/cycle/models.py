from django.db import models

# Create your models here.
class Cycle(models.Model):
    cycledescription = models.TextField()
    cyclestartdate = models.DateField()
    cycleenddate = models.DateField()
    vacationstartdate = models.DateField()
    vacationenddate = models.DateField()
