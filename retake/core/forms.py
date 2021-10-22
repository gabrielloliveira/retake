from django import forms

from retake.core.models import Part


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ("name", "category")
