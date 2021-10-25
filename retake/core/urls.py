from django.urls import path

from retake.core import views

app_name = "core"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("processos/", views.ProcessListView.as_view(), name="list_process"),

    path("partes/", views.PartListView.as_view(), name="list_part"),
    path("partes/criar", views.PartCreateView.as_view(), name="create_part"),
    path("partes/<uuid:uuid>/editar/", views.PartEditView.as_view(), name="edit_part"),
    path("partes/<uuid:uuid>/deletar/", views.PartDeleteView.as_view(), name="delete_part"),
]
