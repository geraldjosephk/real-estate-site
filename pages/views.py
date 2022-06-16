from django.shortcuts import render

# Create your views here.
def index(request):
    """Home Page"""
    return render(request, 'pages/index.html')

def about(request):
    """About Page"""
    return render(request, 'pages/about.html')