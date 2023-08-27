from django.contrib import admin
from .models import Cycle

# Register your models here.


class CycleAdmin(admin.ModelAdmin):
    list_display = (
            'cyclestartdate',
            'cycleenddate',
            'vacationstartdate',
            'vacationenddate',
            )
    # Other configuration options like list_filter, search_fields, etc.

admin.site.register(Cycle, CycleAdmin)
