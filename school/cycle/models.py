from django.db import models

from django.core.exceptions import ValidationError

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
            raise ValidationError("Cycle start date must be before end date")
        
        if self.vacationstartdate >= self.vacationenddate:
            raise ValidationError("Vacation start date must be before end date")

        # Check for overlapping cycles
        overlapping_cycles = Cycle.objects.exclude(pk=self.pk).filter(
            cyclestartdate__lt=self.cycleenddate,
            cycleenddate__gt=self.cyclestartdate
        )

        if overlapping_cycles.exists():
            raise ValidationError("Overlapping cycles are not allowed.")

        # Check for overlapping vacations
        overlapping_vacations = Cycle.objects.exclude(pk=self.pk).filter(
            vacationstartdate__lt=self.vacationenddate,
            vacationenddate__gt=self.vacationstartdate
        )

        if overlapping_vacations.exists():
            raise ValidationError("Overlapping vacations are not allowed.")
