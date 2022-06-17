from django.shortcuts import render

# Create your views here.
def index(request):
    """Listings Page"""
    return render(request, 'listings/listings_index.html')

def listing(request):
    """Listing Page"""
    return render(request, 'listings/listing.html')

def search(request):
    """Search functionality"""
    return render(request, 'listings/search.html')