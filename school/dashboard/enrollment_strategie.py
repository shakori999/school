from ..student.models import Enrollment

class EnrollmentStrategy:
    def enroll(self, course, student):
        pass

class DefaultEnrollmentStrategy(EnrollmentStrategy):
    def enroll(self, course, student):
        Enrollment.objects.create(course=course, student=student)

class PremiumEnrollmentStrategy(EnrollmentStrategy):
    def enroll(self, course, student):
        Enrollment.objects.create(course=course, student=student, premium=True)
