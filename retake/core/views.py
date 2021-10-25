from dal import autocomplete
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from retake.core.forms import PartForm, ProcessForm
from retake.core.models import Process, Part


class IndexView(generic.TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            "count_process": Process.objects.count(),
            "count_parts": Part.objects.count(),
        })
        return context


class ProcessListView(generic.ListView):
    template_name = "process/list.html"
    queryset = Process.objects.order_by("number")


class ProcessDeleteView(generic.DeleteView):
    http_method_names = ["post"]
    success_url = reverse_lazy("core:list_process")
    pk_url_kwarg = 'uuid'

    def get_object(self, queryset=None):
        return get_object_or_404(Process, uuid=self.kwargs['uuid'])

    def delete(self, request, *args, **kwargs):
        super(ProcessDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, "Processo deletado com sucesso.")
        return HttpResponseRedirect(self.success_url)


class ProcessEditView(generic.UpdateView):
    template_name = "process/edit.html"
    form_class = ProcessForm
    pk_url_kwarg = 'uuid'
    success_url = reverse_lazy("core:list_process")

    def get_object(self, queryset=None):
        return get_object_or_404(Process, uuid=self.kwargs['uuid'])

    def form_valid(self, form):
        messages.success(self.request, "Processo editado com sucesso.")
        return super().form_valid(form)


class PartListView(generic.ListView):
    template_name = "part/list.html"
    queryset = Part.objects.order_by("name")

    def get_context_data(self, **kwargs):
        context = super(PartListView, self).get_context_data(**kwargs)
        context.update({
            "form": PartForm(),
        })
        return context


class PartCreateView(generic.CreateView):
    http_method_names = ["post"]
    success_url = reverse_lazy("core:list_part")
    form_class = PartForm

    def form_valid(self, form):
        messages.success(self.request, "Parte cadastrada com sucesso.")
        return super().form_valid(form)


class PartEditView(generic.UpdateView):
    template_name = "part/edit.html"
    form_class = PartForm
    pk_url_kwarg = 'uuid'
    success_url = reverse_lazy("core:list_part")

    def get_object(self, queryset=None):
        return get_object_or_404(Part, uuid=self.kwargs['uuid'])

    def form_valid(self, form):
        messages.success(self.request, "Parte editada com sucesso.")
        return super().form_valid(form)


class PartDeleteView(generic.DeleteView):
    http_method_names = ["post"]
    success_url = reverse_lazy("core:list_part")
    pk_url_kwarg = 'uuid'

    def get_object(self, queryset=None):
        return get_object_or_404(Part, uuid=self.kwargs['uuid'])

    def delete(self, request, *args, **kwargs):
        super(PartDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, "Parte deletada com sucesso.")
        return HttpResponseRedirect(self.success_url)


class PartAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Part.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs
