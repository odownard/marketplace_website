from django.shortcuts import render
from .models import listing

# Create your views here.
def listings_list(request):
    listings = listing.objects.all().order_by('-date')
    return render(request, 'listings/listings.html', { 'listings': listings})