from django.contrib import admin
from .models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'start_date',
            'end_date',
            'teacher',
            'enrollment_strategy'
            )

admin.site.register(Course, CourseAdmin)
