import pytest

@pytest.mark.django_db
def test_test_creation(sample_test):
    assert str(sample_test) ==f"{sample_test.course.name} - Test {sample_test.testno} ({sample_test.testdate} at {sample_test.testtime})" 



@pytest.mark.django_db
def test_testscores_creation(sample_testscore):
    assert str(sample_testscore) ==f"{sample_testscore.student.full_name()} - {sample_testscore.test.course.name} - Test {sample_testscore.testsno}: {sample_testscore.score}" 
