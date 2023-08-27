from django.contrib import admin

# Register your models here.
from .models import Test, TestsScores

# Register your models here.

class TestAdmin(admin.ModelAdmin):
    list_display = ('course', 'cycle', 'enrollment', 'testno', 'testdate' )
    # Other configuration options like list_filter, search_fields, etc.

class TestsScoresAdmin(admin.ModelAdmin):
    list_display = ('course', 'cycle', 'student', 'test', 'score', )
# Register the Student model with its admin class
admin.site.register(Test, TestAdmin)
admin.site.register(TestsScores, TestsScoresAdmin)
