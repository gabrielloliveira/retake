from django.contrib import admin

from retake.core.models import Process, Part


@admin.register(Process)
class ProcessAmin(admin.ModelAdmin):
    list_filter = ["number", "class_name", "subject", "judge"]


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    search_fields = ["name", ]

