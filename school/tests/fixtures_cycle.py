import pytest

from ..cycle.models import Cycle

@pytest.fixture
def cycle():
    cycle =  Cycle.objects.create(
        cycledescription="Sample Cycle",
        cyclestartdate="2023-01-01",
        cycleenddate="2023-12-31",
        vacationstartdate="2023-06-01",
        vacationenddate="2023-06-15",
    )
    return cycle
