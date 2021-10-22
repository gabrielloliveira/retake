from django.views.generic import ListView

from retake.core.models import Process


class ProcessListView(ListView):
    template_name = "core/list.html"
    queryset = Process.objects.order_by("number")

