from django import forms
from .models import PatientRegstration


class PatientRegstrationForm(forms.ModelForm):
    class Meta:
        model = PatientRegstration
        fields = ("patient_id","patient_name","gender","patient_type","age")