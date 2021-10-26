from dal import autocomplete
from django import forms

from retake.core.models import Part, Process


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ("name", "category")


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ("number", "subject", "class_name", "judge", "parts")
        widgets = {
            'parts': autocomplete.ModelSelect2Multiple(url='core:part_autocomplete')
        }


class ProcessAutocompleteForm(forms.ModelForm):
    number = forms.ModelChoiceField(
        queryset=Process.objects.all(),
        widget=autocomplete.ModelSelect2(url='core:process_autocomplete')
    )

    class Meta:
        model = Process
        fields = ("number",)
