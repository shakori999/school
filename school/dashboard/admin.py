from django.contrib import admin
from .models import Person ,Role

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    # Other configuration options like list_filter, search_fields, etc.




# Register the Student model with its admin class
admin.site.register(Role)
admin.site.register(Person, PersonAdmin)
