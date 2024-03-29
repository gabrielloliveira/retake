from django.urls import path

from retake.core import views

app_name = "core"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("processos/", views.ProcessListView.as_view(), name="list_process"),
    path("processos/criar/", views.ProcessCreateView.as_view(), name="create_process"),
    path("processos/<uuid:uuid>/deletar/", views.ProcessDeleteView.as_view(), name="delete_process"),
    path("processos/<uuid:uuid>/editar/", views.ProcessEditView.as_view(), name="edit_process"),
    path("processos/exportar/", views.ProcessExportView.as_view(), name="export_process"),
    path("processos/autocomplete/", views.ProcessAutocomplete.as_view(), name="process_autocomplete"),

    path("partes/", views.PartListView.as_view(), name="list_part"),
    path("partes/criar", views.PartCreateView.as_view(), name="create_part"),
    path("partes/<uuid:uuid>/editar/", views.PartEditView.as_view(), name="edit_part"),
    path("partes/<uuid:uuid>/deletar/", views.PartDeleteView.as_view(), name="delete_part"),
    path("partes/autocomplete/", views.PartAutocomplete.as_view(), name="part_autocomplete"),
]
