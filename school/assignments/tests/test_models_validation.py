import pytest

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError

from ..models import Submission

'''
this section for testing assignment model
'''
# Test Assignment Model Validation
@pytest.mark.django_db
def test_assignment_title_not_empty_validation(assignment_with_empty_title):
    # Attempt to create an assignment with a past due date (which violates the MinValueValidator)
    with pytest.raises(ValidationError) as e:
        assignment_with_empty_title.full_clean()


    # Check that the expected validation error message is raised
    assert "title" in e.value.message_dict

@pytest.mark.django_db
def test_assignment_due_date_validation(assignment_with_invlaid_date):
    invalid_dates = [
        "invalid_date", #not a date
        "22023-08-30",  # Invalid year and day
        "2023-08-32",  # Invalid  day
        "2023-13-15",  # Invalid month
        "2023-02-30",  # February cannot have 30th day
    ]

    for date_str in invalid_dates:
        with pytest.raises(ValidationError) as e:
            assignment_with_invlaid_date.date_of_birth=date_str
            assignment_with_invlaid_date.full_clean()


        assert "due_date" in e.value.error_dict



"""
this section for testing submission model
"""
# Test Submission Model Validation

@pytest.mark.django_db
def test_file_exist(assignment, student):
    with pytest.raises(FileNotFoundError) as e:
        sub = Submission.objects.create(
            assignment = assignment,
            student=student,
            file_upload="b.pdf",
        )
        sub.full_clean()

    assert "No such file or directory" in str(e.value)
    assert sub.submission_date is not None
    assert sub.submission_date >= timezone.now().date()

@pytest.mark.django_db
def test_submission_file_upload_validation(assignment, student):

    with pytest.raises(ValidationError) as e:
        sub = Submission.objects.create(
            assignment=assignment,
            student=student,
            submission_date= timezone.now().date(),  # Submission date is required
            file_upload=None,  # File upload is required
        )
        sub.full_clean()
        

    # Check that the expected validation error message is raised
    assert 'This field cannot be blank.' in str(e.value)

@pytest.mark.django_db
def test_empty_file_upload(student, assignment):
    with pytest.raises(ValidationError) as e:
        sub = Submission.objects.create(
            assignment=assignment,
            student=student,
            file_upload="",  # Empty file_upload field
        )
        sub.full_clean()
    # Check that the expected validation error message is raised
    assert "This field cannot be blank." in str(e.value)


@pytest.mark.django_db
def test_past_submission_date(assignment, student):
    sub = Submission.objects.create(
        assignment = assignment,
        student=student,
        submission_date="2022-08-01",  # Past submission date
        file_upload=SimpleUploadedFile("sub.pdf", b"content"),  # Simulate a file upload
    )
    invalid_dates = [
        "invalid_date", #not a date
        "22023-08-30",  # Invalid year and day
        "2023-08-32",  # Invalid  day
        "2023-13-15",  # Invalid month
        "2023-02-30",  # February cannot have 30th day
    ]

    for date_str in invalid_dates:
        with pytest.raises(ValidationError) as e:
            sub.submission_date=date_str
            sub.full_clean()


    # Check that the expected validation error message is raised
    assert "submission_date" in e.value.error_dict

@pytest.mark.django_db
def test_long_file_name(assignment, student):
    # Create a SimpleUploadedFile instance with a long file name
    long_file_name = "very_long_file_name_that_exceeds_max_length.pdf"
    long_file = SimpleUploadedFile(long_file_name, b'')

    with pytest.raises(ValidationError) as e:
        sub = Submission.objects.create(
            assignment=assignment,
            student=student,
            file_upload=long_file,
        )
        sub.full_clean()

    assert "File name exceeds maximum length of 50 characters" in str(e.value)

@pytest.mark.django_db
def test_file_upload_with_unsupported_type(assignment, student):

    # Create a SimpleUploadedFile instance with an unsupported file type
    unsupported_file = SimpleUploadedFile("unsupported_image.jpg", b'')

    with pytest.raises(ValidationError) as e:
        sub = Submission.objects.create(
            assignment = assignment,
            student=student,
            file_upload=unsupported_file,  # Unsupported file type
        )
        sub.full_clean()

    # Check that the expected validation error message is raised
    assert "Unsupported file format. Supported formats: .pdf, .doc, .docx']" in str(e.value)

@pytest.mark.django_db
def test_file_max_size_exceeded(assignment, student):

    # Create content that exceeds the maximum allowed size
    oversized_content = b'X' * (10 * 1024 * 1024 + 1)  # Create content exceeding 10 MB

    # Create a ContentFile instance with the oversized content
    oversized_file = ContentFile(oversized_content, name="oversized_file.pdf")

    with pytest.raises(ValidationError) as e:
        sub = Submission(
            assignment=assignment,
            student=student,
            file_upload=oversized_file,
        )
        sub.full_clean()

    # Check that the expected validation error message is raised
    assert "File size exceeds the maximum allowed size of 10485760 bytes." in str(e.value)

