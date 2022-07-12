from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import state_choices,bedroom_choices,price_choices

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
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    """Search functionality"""
    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices' : price_choices,
        'state_choices' : state_choices
    }
    return render(request, 'listings/search.html',context)