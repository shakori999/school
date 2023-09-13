from rest_framework import serializers
from .models import Cycle

class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        """
        Custom validation for the serializer data.
        """
        cyclestartdate = data.get('cyclestartdate')
        cycleenddate = data.get('cycleenddate')
        vacationstartdate = data.get('vacationstartdate')
        vacationenddate = data.get('vacationenddate')

        if cyclestartdate >= cycleenddate:
            raise serializers.ValidationError("Cycle start date must be before end date")

        if vacationstartdate >= vacationenddate:
            raise serializers.ValidationError("Vacation start date must be before end date")

        # Check for overlapping cycles
        overlapping_cycles = Cycle.objects.exclude(pk=self.instance.pk if self.instance else None).filter(
            cyclestartdate__lt=cycleenddate,
            cycleenddate__gt=cyclestartdate
        )

        if overlapping_cycles.exists():
            raise serializers.ValidationError("Overlapping cycles are not allowed.")

        # Check for overlapping vacations
        overlapping_vacations = Cycle.objects.exclude(pk=self.instance.pk if self.instance else None).filter(
            vacationstartdate__lt=vacationenddate,
            vacationenddate__gt=vacationstartdate
        )

        if overlapping_vacations.exists():
            raise serializers.ValidationError("Overlapping vacations are not allowed.")

        return data
