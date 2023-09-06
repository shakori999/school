import pytest

from datetime import date

from django.core.exceptions import ValidationError

from ..models import Cycle

@pytest.mark.django_db
def test_cycle_start_date_before_end_date():
    # Test valid data: Cycle start date before cycle end date
    cycle = Cycle(
        cycledescription="Test Cycle",
        cyclestartdate="2023-09-01",
        cycleenddate="2023-12-31",
        vacationstartdate="2023-08-01",
        vacationenddate="2023-08-15",
    )
    cycle.full_clean()  # Should not raise a ValidationError

@pytest.mark.django_db
def test_vacation_start_date_before_end_date():
    # Test valid data: Vacation start date before vacation end date
    cycle = Cycle(
        cycledescription="Test Cycle",
        cyclestartdate="2023-09-01",
        cycleenddate="2023-12-31",
        vacationstartdate="2023-08-01",
        vacationenddate="2023-08-15",
    )
    cycle.full_clean()  # Should not raise a ValidationError

@pytest.mark.django_db
def test_no_overlapping_cycles():
    # Test invalid data: Overlapping cycles
    with pytest.raises(ValidationError) as e:
        # Create an existing cycle
        existing_cycle = Cycle.objects.create(
            cycledescription="Existing Cycle",
            cyclestartdate="2023-09-01",
            cycleenddate="2023-12-31",
            vacationstartdate="2023-08-01",
            vacationenddate="2023-08-15",
        )
        # Attempt to create a new cycle overlapping with the existing cycle
        new_cycle = Cycle(
            cycledescription="Overlapping Cycle",
            cyclestartdate="2023-11-01",  # Overlapping start date
            cycleenddate="2024-01-31",  # Overlapping end date
            vacationstartdate="2023-09-01",
            vacationenddate="2023-09-15",
        )
        new_cycle.full_clean()

    # Ensure that the validation error message is as expected
    assert "Overlapping cycles are not allowed." in str(e.value)

# Similar tests can be written for 'test_no_overlapping_vacations' and 'test_clean_method_works'.


@pytest.mark.django_db
def test_no_overlapping_vacations():
    # Test invalid data: Overlapping vacations
    with pytest.raises(ValidationError) as e:
        # Create an existing cycle with vacation dates
        existing_cycle = Cycle.objects.create(
            cycledescription="Existing Cycle",
            cyclestartdate=date(2023, 9, 1),
            cycleenddate=date(2023, 12, 31),
            vacationstartdate=date(2023, 8, 1),
            vacationenddate=date(2023, 8, 15),
        )
        # Attempt to create a new cycle overlapping with the existing vacation
        new_cycle = Cycle(
            cycledescription="Overlapping Vacation Cycle",
            cyclestartdate=date(2024, 1, 1),
            cycleenddate=date(2024, 4, 30),
            vacationstartdate=date(2023, 8, 10),
            vacationenddate=date(2023, 9, 10),
        )
        new_cycle.full_clean()

    # Ensure that the validation error message is as expected
    assert "Overlapping vacations are not allowed." in str(e.value)

@pytest.mark.django_db
def test_clean_method_works():
    # Test invalid data: Cycle start date after cycle end date
    with pytest.raises(ValidationError) as e:
        # Attempt to create a cycle with invalid date ranges
        invalid_cycle = Cycle(
            cycledescription="Invalid Cycle",
            cyclestartdate="2023-12-31",  # Invalid start date
            cycleenddate="2023-09-01",  # Invalid end date
            vacationstartdate="2023-08-01",
            vacationenddate="2023-08-15",
        )
        invalid_cycle.full_clean()

    # Ensure that the validation error message is as expected
    assert "Cycle start date must be before end date" in str(e.value)
