from django.views.generic import ListView, TemplateView

from retake.core.models import Process, Part


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            "count_process": Process.objects.count(),
            "count_parts": Part.objects.count(),
        })
        return context


class ProcessListView(ListView):
    template_name = "process/list.html"
    queryset = Process.objects.order_by("number")

