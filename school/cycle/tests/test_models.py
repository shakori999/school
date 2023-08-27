import pytest


@pytest.mark.django_db
def test_cycle_creation(cycle):
    assert str(cycle) == f"Cycle: {cycle.cyclestartdate} to {cycle.cycleenddate}"

