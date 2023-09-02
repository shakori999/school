import pytest

@pytest.mark.django_db
def test_class_creation(sample_class):
    assert str(sample_class) == f"{sample_class.classtitle} ({sample_class.classdate} - {sample_class.starttime} to {sample_class.endtime})"


