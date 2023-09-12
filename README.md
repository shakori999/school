# school_management_system

The School Admin System is a comprehensive administrative tool designed to streamline and simplify school management processes. It serves as a central hub for managing student information, courses, assignments, attendance, and more. Developed using Django, a high-level Python web framework, this system empowers educational institutions with efficient tools for tracking student progress, automating administrative tasks, and enhancing communication between staff, students, and parents.

Key Features:

    Student Management: Easily manage student records, including personal information, enrollment, and attendance.

    Course Management: Create, update, and track courses and class schedules.

    Assignment Tracking: Assign and monitor student assignments with due dates, descriptions, and file uploads.

    Attendance Tracking: Keep accurate attendance records and generate reports for analysis.

    User-Friendly Interface: An intuitive and user-friendly web interface for both administrators and end-users.

    Customization: Adapt the system to your school's specific needs with easy-to-configure settings.

    Security: Implement role-based access control to safeguard sensitive data.

    Scalability: Designed for scalability, making it suitable for schools of all sizes.

The School Admin System aims to improve efficiency, transparency, and communication within educational institutions, ultimately enhancing the learning experience for students and easing the workload for administrators.

Built with love by [murtatha](https://www.github.com/shakori999/).

## Table of Contents

- [Checklist](#checklist)
- [Installation](#installation)
  - [Django Installation](#django-installation)
  - [Pytest Installation](#pytest-installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Checklist

Use this checklist to keep track of the components you've created and tested:

### Models

- [x] Create models for

#### Assignments
- [x] `Assignment`
- [x] `Submission`

#### Attendance
- [x] `Attendance`

#### Categories
- [x] `Category`

#### Classes
- [x] `Class`

#### Course
- [x] `Course`
- [x] `CoursesPerCycle`

#### Cycle
- [x] `Cycle`

#### Dashboard
- [x] `Role`
- [x] `BaseModel`
- [x] `Person`

#### Exams
- [x] `Test`
- [x] `TestScores`

#### Student
- [x] `Student`
- [x] `Enrollment`

#### Teacher
- [x] `Teacher`
- [x] `TeachersPerCourse`

- [x] Define necessary fields and relationships for each model.
- [x] Run migrations to create database tables.
- [ ] create more models.
- [ ] link them better.

### Tests

- [x] Write unit tests for models using pytest and Django's TestCase.
- [x] Test model creation. Completed all. 
- [x] Test model String Representation. Completed all.
- [x] Test model validation. Completed all. 
- [ ] Test model Data Integrity.`assignment, submission, attendance, Role, person`
- [ ] Test model relationships. Completed only for:`person, Teacher, student` 
- [ ] Test model methods and properties. Completed only for:`person, Teacher` 
- [ ] Test model Index. Completed only for: `person`
- [ ] Test model signal.
- [ ] Test model Meta Options.
- [ ] Test model Model Manager.
- [ ] Test model Integration.

### Fixtures

- [x] Create fixtures for models using pytest fixtures.
- [x] Include sample data for each model to be used in tests.

### Serializers 

- [x] Create serializers for `Assignment` model
- [x] Create serializers for `Submission` model
- [x] Create serializers for `Attendance` model
- [ ] Create serializers for `Category` model
- [ ] Create serializers for `Class` model
- [ ] Create serializers for `Course` model
- [ ] Create serializers for `CoursesPerCycle` model
- [ ] Create serializers for `Cycle` model
- [ ] Create serializers for `Role` model
- [ ] Create serializers for `Person` model
- [ ] Create serializers for `Test` model
- [ ] Create serializers for `TestScores` model
- [ ] Create serializers for `Student` model
- [ ] Create serializers for `Enrollment` model
- [ ] Create serializers for `Teacher` model
- [ ] Create serializers for `TeachersPerCourse` model

# Testing Serializers

Testing serializers is crucial to ensure your Django project's API behaves correctly and handles data validation and conversion accurately. This section outlines the steps to test your serializers using pytest and Django's TestCase.

## Testing Checklist

Follow this checklist to thoroughly test your serializers:

- [ ] **Test Serializer Validation**:
  - Create tests to ensure the serializer handles valid data correctly.

- [ ] **Test Serializer Validation Errors**:
  - Write tests to check whether the serializer catches validation errors for invalid data.

- [ ] **Test Serializer Data Conversion**:
  - Verify that the serializer correctly converts Python data objects to JSON and vice versa.

- [ ] **Test Serializer Save Method**:
  - If applicable, write tests to validate the serializer's `create` or `update` methods for model instances.

- [ ] **Test Serializer Context**:
  - If your serializer relies on context data (e.g., current user), create tests to ensure it handles this data correctly.

- [ ] **Test Serializer Fields**:
  - Check whether the serializer includes the expected fields and handles field validation and conversion correctly.

- [ ] **Test Serializer Nested Objects**:
  - Verify that the serializer correctly handles nested objects, such as related models.

- [ ] **Test Serializer Data Integrity**:
  - Ensure that the serializer maintains data integrity, especially for related objects.

- [ ] **Test Serializer Meta Options**:
  - If you've customized the serializer's `Meta` class, ensure that the specified options are correctly applied.

- [ ] **Test Serializer Integration**:
  - Write integration tests that use the serializer within your API views to ensure correct API behavior.

- [ ] **Test Serializer Edge Cases**:
  - Identify and test edge cases that might cause issues with your serializer.

- [ ] **Test Serializer Nested Validations**:
  - If your serializer includes nested serializers, create tests to validate nested data and nested validations.

## Running Tests

To run your serializer tests, use pytest or Django's TestCase. Make sure your tests cover various scenarios, including common cases, edge cases, and error handling.

# Run tests with pytest
pytest your_app/tests/test_serializers.py

# Run tests with Django's TestCase
python manage.py test your_app.tests.test_serializers


### Views and Templates 

- [x] Create views for `Assignment` model (List, Detail, Create, Update, Delete)
- [x] Create views for `Submission` model (List, Detail, Create, Update, Delete)
- [x] Create views for `Attendance` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `Category` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `Class` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `Course` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `CoursesPerCycle` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `Cycle` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `Role` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `BaseModel` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `Person` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `Test` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `TestScores` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `Student` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `Enrollment` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `Teacher` model (List, Detail, Create, Update, Delete)
- [ ] Create views for `TeachersPerCourse` model (List, Detail, Create, Update, Delete)
- [ ] Create views for displaying data in your application.
- [ ] Design templates for rendering the data in a user-friendly way.

### URLs and Routing 

- [ ] Define URL patterns for your application's views.
- [ ] Set up routing to connect URLs to views.

### README

- [x] Update this README with a description of the project.
- [x] Include the checklist to keep track of completed tasks.
- [ ] Add installation instructions, usage guide, and any other relevant information.

### Documentation

- [ ] Provide detailed documentation for your models, functions, and classes.
- [ ] Include instructions for setting up and running the project locally.
- [ ] Explain how to run tests and what they cover.

## Installation

prerequisites, virtual environment setup, and any dependencies needed.

### Django Installation

1. Ensure you have Python installed. You can download it from the official [Python website](https://www.python.org/downloads/).

2. Install Django using pip:


### Pytest Installation

1. Install pytest using pip:
2. Install pytest-django for integrating pytest with Django:

## Usage

Provide code examples, command-line usage, or screenshots if applicable.

## Testing
information on running individual tests, test coverage, and continuous integration.

To run tests using pytest, follow these steps:

1. Navigate to the root directory of your project in the terminal.

2. Run the following command to execute all tests:

3. To run specific tests, use the following command:

## Contributing

how others can contribute to my project. Include guidelines for submitting pull requests, reporting issues, and code review process.

## License

Specify the license under which your project is released. Include any third-party libraries or assets and their licenses if applicable.

