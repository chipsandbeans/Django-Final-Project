from django import forms
from .models import WeightTracking

class WeightTrackingForm(forms.ModelForm):
    class Meta:
        model = WeightTracking
        fields = ['weight', 'unit']