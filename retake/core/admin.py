from django.contrib import admin
from django.http import HttpResponse

from retake.core.models import Process, Part
from retake.core.utils import build_csv_process


@admin.register(Process)
class ProcessAmin(admin.ModelAdmin):
    list_display = ["number", "class_name", "subject", "judge"]
    list_filter = ["number", "class_name"]
    search_fields = ["number", "parts__name__icontains", "judge"]
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="processos.csv"'},
        )
        build_csv_process(response, queryset)
        return response

    export_to_csv.short_description = "Exportar para CSV"


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    search_fields = ["name", ]
    list_display = ["name", "category"]
    list_filter = ["category"]
