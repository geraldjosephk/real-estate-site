from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    """Listings Page"""
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }
    return render(request, 'listings/listings_index.html', context)

def listing(request,listing_id):
    """Listing Page"""
    return render(request, 'listings/listing.html')

def search(request):
    """Search functionality"""
    return render(request, 'listings/search.html')