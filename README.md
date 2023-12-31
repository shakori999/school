# School Management System

The School Admin System is a comprehensive administrative tool designed to streamline and simplify school management processes. It serves as a central hub for managing student information, courses, assignments, attendance, and more. Developed using Django, a high-level Python web framework, this system empowers educational institutions with efficient tools for tracking student progress, automating administrative tasks, and enhancing communication between staff, students, and parents.

**Key Features:**

- Student Management: Easily manage student records, including personal information, enrollment, and attendance.
- Course Management: Create, update, and track courses and class schedules.
- Assignment Tracking: Assign and monitor student assignments with due dates, descriptions, and file uploads.
- Attendance Tracking: Keep accurate attendance records and generate reports for analysis.
- User-Friendly Interface: An intuitive and user-friendly web interface for both administrators and end-users.
- Customization: Adapt the system to your school's specific needs with easy-to-configure settings.
- Security: Implement role-based access control to safeguard sensitive data.
- Scalability: Designed for scalability, making it suitable for schools of all sizes.

The School Admin System aims to improve efficiency, transparency, and communication within educational institutions, ultimately enhancing the learning experience for students and easing the workload for administrators.

Built with hate by [murtatha](https://www.github.com/shakori999/).

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

- [x] Create models for:
  - [x] `Assignment`
  - [x] `Submission`
  - [x] `Attendance`
  - [x] `Category`
  - [x] `Class`
  - [x] `Course`
  - [x] `CoursesPerCycle`
  - [x] `Cycle`
  - [x] `Dashboard`
  - [x] `Role`
  - [x] `BaseModel`
  - [x] `Person`
  - [x] `Exams`
  - [x] `Test`
  - [x] `TestScores`
  - [x] `Student`
  - [x] `Enrollment`
  - [x] `Teacher`
  - [x] `TeachersPerCourse`
  - [x] `Lesson`
  - [x] `LessonPDF`
  
- [x] Define necessary fields and relationships for each model.
- [x] Run migrations to create database tables.
- [ ] Create more models.
- [ ] Link them better.

### Serializers 

- [x] Create serializers for all models. `Completed all.` 

### Views and Templates 

- [x] Create views for all models (List, Detail, Create, Update, Delete)
- [ ] Create views for displaying data in your application.
- [ ] Design templates for rendering the data in a user-friendly way.

### URLs and Routing 

- [x] Define URL patterns for your application's views.
- [ ] Set up routing to connect URLs to views.

### Fixtures

- [x] Create fixtures for models using pytest fixtures.
- [x] Include sample data for each model to be used in tests.

# Testing Serializers

Testing serializers is crucial to ensure your Django project's API behaves correctly and handles data validation and conversion accurately. This section outlines the steps to test your serializers using pytest and Django's TestCase.

### Testing Models

- [x] Write unit tests for models using pytest and Django's TestCase.
- [x] Test model creation. Completed all.
- [x] Test model String Representation. Completed all.
- [x] Test model validation. Completed all.
- [ ] Test model Data Integrity (e.g., `assignment`, `submission`, `attendance`, `Role`, `person`).
- [ ] Test model relationships. Completed only for: `person`, `Teacher`, `student`.
- [ ] Test model methods and properties. Completed only for: `person`, `Teacher`.
- [ ] Test model Index. Completed only for: `person`.
- [ ] Test model Meta Options. `student`.
- [ ] Test model signal.
- [ ] Test model Model Manager.
- [ ] Test model Integration.

## Testing Serializers

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

### README

- [x] Update this README with a description of the project.
- [x] Include the checklist to keep track of completed tasks.
- [ ] Add installation instructions, usage guide, and any other relevant information.

### Documentation

- [ ] Provide detailed documentation for your models, functions, and classes.
- [ ] Include instructions for setting up and running the project locally.
- [ ] Explain how to run tests and what they cover.

## Installation

Follow these steps to set up your project:
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

## Running Tests

To run your serializer tests, use pytest or Django's TestCase. Make sure your tests cover various scenarios, including common cases, edge cases, and error handling.

# Run tests with pytest
pytest your_app/tests/test_serializers.py

# Run tests with Django's TestCase
python manage.py test your_app.tests.test_serializers

## Contributing

how others can contribute to my project. Include guidelines for submitting pull requests, reporting issues, and code review process.

## License

Specify the license under which your project is released. Include any third-party libraries or assets and their licenses if applicable.

