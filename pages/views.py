from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices,price_choices,bedroom_choices


# Create your views here.
def index(request):
    """Home Page"""
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices' : price_choices,
        'state_choices' : state_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    """About Page"""
    #All realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #MVP realtor
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'pages/about.html', context)