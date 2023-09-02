import pytest

from ..exames.models import Test, TestsScores

@pytest.fixture
def sample_test(course, cycle,enrollment):
    test =  Test.objects.create(
        course = course,
        cycle = cycle,
        enrollment=enrollment,
        testno = "1",
        testdate = "2023-06-15",
        testtime = "10:23:02",
        agenda = "this is a good test",
    )
    return test

@pytest.fixture
def sample_testscore(course, cycle,student, sample_test):
    testscore =  TestsScores.objects.create(
        course = course,
        cycle = cycle,
        student = student,
        test = sample_test,
        testsno = "2",
        score = "30",
    )
    return testscore


