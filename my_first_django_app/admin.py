from django.contrib import admin

# Register your models here.
from django.utils import timezone

from . import models


def mark_complete(model_admin, request, queryset):
    # Used to customize the dropdown in TABLE page
    queryset.update(status=models.Task.TaskStatus.COMPLETED,
                    completed_at=timezone.now())


def mark_pending(model_admin, request, queryset):
    # Used to customize the dropdown in TABLE page
    queryset.update(status=models.Task.TaskStatus.PENDING,
                    completed_at=None)


# Adding a short description to the dropdown in a respective Table page
mark_pending.short_description = "Mark these task as PENDING"


class TaskAdmin(admin.ModelAdmin):
    # We can manipulate the fields to be shown when we are creating a record
    fields = ['content', 'deadline', 'tags']

    # Add attributes on the main page of the table
    # We can add attributes and properties
    list_display = ['content', 'status', 'created_at', 'foo', 'get_all_tags']

    # We can make the attributes / properties in the list_display editable
    # The attributes / properties mentioned here has to be mandatory present in list_display
    list_editable = ['status']

    actions = [mark_complete, mark_pending]

    # Create a filter to filters the documents to be displayed
    # We can have more than 1 filter
    list_filter = ['status', 'tags']

    # Create a search field
    search_fields = ['content', 'tags__name']

    # Display the records in a certain order
    # Approach - 1
    # ordering = ['deadline']

    # Approach -2
    def get_ordering(self, request):
        if request.user.is_superuser:
            return ['status']
        else:
            return ['deadline']


admin.site.register(models.Tag)
admin.site.register(models.Task, TaskAdmin)
