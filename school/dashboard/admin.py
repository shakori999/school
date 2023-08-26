from django.contrib import admin
from .models import Person, Enrollment

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    # Other configuration options like list_filter, search_fields, etc.


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'premium')
    # Other configuration options like list_filter, search_fields, etc.

# Register the Student model with its admin class
admin.site.register(Person, PersonAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
