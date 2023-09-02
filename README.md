# school_management_system

Description of your project.

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
- [x] Test model creation. completed. 
- [x] Test model String Representation. completed only for:`person, Teacher, student` 
- [ ] Test model relationships. completed only for:`person, Teacher, student` 
- [ ] Test model validation. completed only for: `person, Teacher` 
- [ ] Test model methods and properties. completed only for:`person, Teacher` 
- [ ] Test model signal.
- [ ] Test model Index. completed only for: `person`
- [ ] Test model Meta Options.
- [ ] Test model Model Manager.
- [ ] Test model Data Integrity.
- [ ] Test model Integration.

### Fixtures

- [x] Create fixtures for models using pytest fixtures.
- [x] Include sample data for each model to be used in tests.

### Views and Templates 

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

