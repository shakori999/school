import pytest

from django.db.utils import IntegrityError
from django.db import transaction

from ..models import Role, Person

'''
this section for testing Person model
'''

@pytest.mark.django_db
def test_role_name_uniqueness():
    # Create a role with a unique name
    Role.objects.create(role_name="UniqueRole")

    # Try to create another role with the same name
    with pytest.raises(IntegrityError):
        Role.objects.create(role_name="UniqueRole")

'''
this section for testing Person model
'''

@pytest.mark.django_db
def test_person_role_assignment(user_student):

    with pytest.raises(IntegrityError):
        person = Person(
            user=user_student,
            username="user",
            password_hash="password",
            email="user@example.com",
            role=None,
        )
        person.save()


    
