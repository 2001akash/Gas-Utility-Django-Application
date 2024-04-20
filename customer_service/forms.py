from django import forms
from .models import ServiceRequest

# Form for creating a new service request
class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachment']
