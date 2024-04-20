from django.urls import path
from . import views  # Ensure this import works correctly

urlpatterns = [
    path('track_requests/', views.track_requests, name='track_requests'),
    path('submit_request/', views.submit_request, name='submit_request'),  # Make sure 'submit_request' is defined
]
