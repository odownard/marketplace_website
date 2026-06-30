from django.shortcuts import render, redirect
from .models import Listing
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q
from .filters import ListingFilter

# Create your views here.
# def listings_list(request):
#     listings = Listing.objects.all().order_by('-date')
#     return render(request, 'listings/listings.html', {'listings': listings})

def listing_page(request, slug):
    listing = Listing.objects.get(slug=slug)
    return render(request, 'listings/listing_page.html', {'listing': listing})

@login_required(login_url="/users/login/")
def listing_new(request):
    if request.method == 'POST':
        form = forms.CreateListing(request.POST, request.FILES)
        if form.is_valid():
            # Save with user
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('listings:list')
    else: 
        form = forms.CreateListing()
    return render(request, 'listings/listing_new.html', { 'form': form })

def list(request):
    query = request.GET.get('search', '')
    if query == '':
        queryset = Listing.objects.all()
    else:
        queryset = Listing.objects.filter(
            Q(title__icontains=query)
            )
        
    listing_filter = ListingFilter(request.GET, queryset=queryset)

    context = {
        'query': query,
        'filter': listing_filter,
        'results': listing_filter.qs
    }
    return render(request, 'listings/listings.html', context)