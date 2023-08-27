from django.contrib import admin
from .models import Class
# Register your models here.
class ClassAdmin(admin.ModelAdmin):
    list_display = (
            'classtitle',
            'coursespercycle',
            'classno',
            'classdate',
            'course',
            'cycle',
            )

admin.site.register(Class, ClassAdmin)
