from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.listings_list, name="list"),
    path('new-listing/', views.listing_new, name="new-listing"),
    path('<slug:slug>', views.listing_page, name="page"),
]
