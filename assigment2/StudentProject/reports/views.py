from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def reports_view(request):
    return render(request, 'reports/index.html')
