from django.shortcuts import render

# Create your views here.
def listings_list(request):
    return render(request, 'listings/listings.html')