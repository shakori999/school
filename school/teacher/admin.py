from django.contrib import admin
from .models import Teacher, TeachersPerCourse

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject_taught')
    # Other configuration options like list_filter, search_fields, etc.

class TeachersPerCourseAdmin(admin.ModelAdmin):
    list_display = ('cycle', 'teacher', 'coursespercycle',)
    # Other configuration options like list_filter, search_fields, etc.

# Register the Student model with its admin class
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeachersPerCourse, TeachersPerCourseAdmin)
