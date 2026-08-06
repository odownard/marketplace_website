# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from listings.models import Listing


def homepage(request):
    homepage_categories = Listing.CATEGORY_CHOICES

    homepage_listings = Listing.objects.all().order_by('-date')

    context = {
        'categories': homepage_categories,
        'listings': homepage_listings
    }
    return render(request, 'home.html', context)

@login_required(login_url="/users/login/")
# def my_account(request):
# #    return HttpResponse("My Account Page.")
#     return render(request, 'my_account.html')

def my_listings(request):
    # for listing in listings: 
    #     if user == listing(user):
    #         my_listings = my_listings + listing
    my_listings = Listing.objects.filter(author=request.user).order_by('-date')

    context = {
        'my_listings':my_listings
    }
    return render(request, 'my_account.html', context)