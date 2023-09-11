from django.contrib import admin
from .models import Assignment, Submission

# Register your models here.
class AssignmentAdmin(admin.ModelAdmin):
    list_display = (
            'course',
            'title',
            "due_date",
            )

class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
            'assignment',
            'student',
            "file_upload",
            )

admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Submission, SubmissionAdmin)

