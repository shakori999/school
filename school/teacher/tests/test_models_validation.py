import pytest
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_teacher_invalid_username(teacher_invalid_username):
    with pytest.raises(ValidationError) as e:
        teacher_invalid_username.full_clean()
        print(f"show me :{teacher_invalid_username}")
    
    assert "teachername" in e.value.message_dict

@pytest.mark.django_db
def test_teacher_invalid_email(teacher_invalid_email):
    with pytest.raises(ValidationError) as e:
        teacher_invalid_email.full_clean()
    
    assert "email" in e.value.message_dict

@pytest.mark.django_db
def test_teacher_invalid_phoneno(teacher_invalid_phoneno):
    with pytest.raises(ValidationError) as e:
        teacher_invalid_phoneno.full_clean()

    assert "phoneno" in e.value.message_dict

@pytest.mark.django_db
def test_teacher_invalid_subject_taught(teacher_invalid_subject_taught):
    with pytest.raises(ValidationError) as e:
        teacher_invalid_subject_taught.full_clean()

    assert "subject_taught" in e.value.message_dict

@pytest.mark.django_db
def test_teacher_invalid_date_of_birth(teacher_invalid_date_of_birth):
    with pytest.raises(ValidationError) as e :
        teacher_invalid_date_of_birth.full_clean()

    assert "date_of_birth" in e.value.message_dict

@pytest.mark.django_db
def test_teacher_invalid_address(teacher_invalid_address):
    with pytest.raises(ValidationError) as e:
        teacher_invalid_address.full_clean()

    assert "address" in e.value.message_dict
