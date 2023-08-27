from django.db import models

# Create your models here.
class Cycle(models.Model):
    cycledescription = models.TextField()
    cyclestartdate = models.DateField()
    cycleenddate = models.DateField()
    vacationstartdate = models.DateField()
    vacationenddate = models.DateField()

    class Meta:
        ordering = ['cyclestartdate']

    def __str__(self):
        return f"Cycle: {self.cyclestartdate} to {self.cycleenddate}"

    def clean(self):
        if self.cyclestartdate >= self.cycleenddate:
            raise models.ValidationError("Cycle start date must be before end date")
        
        if self.vacationstartdate >= self.vacationenddate:
            raise models.ValidationError("Vacation start date must be before end date")
