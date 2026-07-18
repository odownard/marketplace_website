# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from listings.models import Listing


def homepage(request):
    homepage_categories = Listing.CATEGORY_CHOICES
    context = {
        'categories': homepage_categories
    }
    return render(request, 'home.html', context)

@login_required(login_url="/users/login/")
def my_account(request):
#    return HttpResponse("My Account Page.")
    return render(request, 'my_account.html')