from django.shortcuts import render
from .models import Listing
from django.contrib.auth.decorators import login_required

# Create your views here.
def listings_list(request):
    listings = Listing.objects.all().order_by('-date')
    return render(request, 'listings/listings.html', {'listings': listings})

def listing_page(request, slug):
    listing = Listing.objects.get(slug=slug)
    return render(request, 'listings/listing_page.html', {'listing': listing})

@login_required(login_url="/users/login/")
def listing_new(request):
    return render(request, 'listings/listing_new.html')