from django.contrib import admin
from .models import Course, CoursesPerCycle

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = (
            'code',
            'category',
            )

class CoursesPerCycleAdmin(admin.ModelAdmin):
    list_display = (
            'course',
            'cycle',
            'coursestartdate',
            )

admin.site.register(Course, CourseAdmin)
admin.site.register(CoursesPerCycle, CoursesPerCycleAdmin)
