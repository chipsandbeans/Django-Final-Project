from django import forms
from .models import WeightTracking


# Weight Tracking Form
class WeightTrackingForm(forms.ModelForm):
    class Meta:
        model = WeightTracking
        fields = ['weight', 'unit']