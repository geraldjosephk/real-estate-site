from django.shortcuts import render
from .models import Listing

# Create your views here.
def index(request):
    """Listings Page"""
    listings = Listing.objects.all()

    context = {
        'listings': listings
    }
    return render(request, 'listings/listings_index.html', context)

def listing(request,listing_id):
    """Listing Page"""
    return render(request, 'listings/listing.html')

def search(request):
    """Search functionality"""
    return render(request, 'listings/search.html')