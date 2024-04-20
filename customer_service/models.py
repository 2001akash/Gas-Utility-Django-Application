from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Status choices for service requests
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Resolved', 'Resolved'),
]

class ServiceRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)  # For tracking resolution
    attachment = models.FileField(upload_to='service_attachments/', blank=True, null=True)

    def __str__(self):
        return f"{self.request_type} - {self.customer.username} - {self.status}"
