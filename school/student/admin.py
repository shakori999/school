from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', )
    # Other configuration options like list_filter, search_fields, etc.

# Register the Student model with its admin class
admin.site.register(Student, StudentAdmin)
