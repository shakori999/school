import pytest

@pytest.mark.django_db
def test_attendence_creation(attendance):
    assert str(attendance) ==f"{attendance.student.full_name()} - {attendance.class_info.classtitle} ({attendance.class_info.classdate})" 

        
