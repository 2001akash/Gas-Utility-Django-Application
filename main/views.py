
# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')  # This should point to the homepage template
