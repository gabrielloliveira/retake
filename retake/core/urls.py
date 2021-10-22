from django.urls import path

from retake.core import views

app_name = "core"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("processos/", views.ProcessListView.as_view(), name="list_process"),
]
