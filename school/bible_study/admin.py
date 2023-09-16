from django.contrib import admin
from .models import Lesson,LessonPDF
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = (
            'class_info',
            'lesson_number',
            'lesson_name',
            'verse_to_memorize',
            'chapters_to_read',
            )

class LessonPDFAdmin(admin.ModelAdmin):
    list_display = (
            'lesson',
            'pdf_file',
            )


admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonPDF, LessonPDFAdmin)
