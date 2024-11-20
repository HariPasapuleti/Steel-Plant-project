from django import forms
from .models import Machine

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'model', 'company', 'description', 'image', 'latitude', 'longitude', 'complaints']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'complaints': forms.Textarea(attrs={'rows':4, 'cols': 40})
        }
