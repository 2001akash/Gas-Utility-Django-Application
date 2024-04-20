from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest  # Correct import
from django.core.paginator import Paginator  # Optional: for pagination

@login_required
def track_requests(request):
    # Fetch all service requests for the logged-in user, ordered by creation time
    requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')

    # Optional: Pagination for easier viewing
    paginator = Paginator(requests, 10)  # 10 requests per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render the view with a list of requests
    return render(
        request, 
        'customer_service/track_requests.html', 
        {'requests': page_obj}  # Use page_obj if paginated
    )

from .forms import ServiceRequestForm  # Ensure you have a form for submitting requests

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user  # Associate with the logged-in user
            service_request.save()
            return redirect('track_requests')  # Redirect to the tracking page after submission
    else:
        form = ServiceRequestForm()

    return render(request, 'customer_service/submit_request.html', {'form': form})
