from django.contrib import admin
from .models import Student, Enrollment

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthdate' )
    # Other configuration options like list_filter, search_fields, etc.

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course_per_cycle', 'student', 'enrollmentdate', )
# Register the Student model with its admin class
admin.site.register(Student, StudentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
