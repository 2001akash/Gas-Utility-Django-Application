from django.contrib import admin
from .models import ServiceRequest
from django.utils import timezone

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['request_type', 'customer', 'status', 'created_at', 'updated_at', 'resolved_at']
    search_fields = ['request_type', 'customer__username']

    def save_model(self, request, obj, form, change):
        # If status is being updated to 'Resolved', set resolved_at to now
        if 'status' in form.changed_data and obj.status == 'Resolved':
            obj.resolved_at = timezone.now()  # Set the resolved date and time
        super().save_model(request, obj, form, change)

admin.site.register(ServiceRequest, ServiceRequestAdmin)
