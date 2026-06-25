import django_filters
from .models import Listing

class ListingFilter(django_filters.FilterSet):
    # #Title Search
    # title_search = django_filters.CharFilter()

    #Price Filters
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    CATEGORY_CHOICES = [
        ('Sports', 'Sports'),
        ('Electronics', 'Electronics'),
        ('Motors', 'Motors'),
        ('Fashion', 'Fashion'),
        ('Art/Music', 'Art/Music'),
        ('Property', 'Property'),
        ('Health', 'Health'),
        ('Other', 'Other')
    ]

    #Category Filter
    category = django_filters.ChoiceFilter(field_name='category', lookup_expr='exact', choices=CATEGORY_CHOICES)

    LOCATION_CHOICES = [
        ('Northland', 'Northland'),
        ('Auckland', 'Auckland'),
        ('Waikato', 'Waikato'),
        ('Bay Of Plenty', 'Bay Of Plenty'),
        ('Gisborne', 'Gisborne'),
        ("Hawke's Bay", "Hawke's Bay"),
        ('Taranaki', 'Taranaki'),
        ('Manawatū-Whanganui', 'Manawatū-Whanganui'),
        ('Wellington', 'Wellington'),
        ('Tasman', 'Tasman'),
        ('Nelson', 'Nelson'),
        ('Marlborough', 'Marlborough'),
        ('West Coast', 'West Coast'),
        ('Canterbury', 'Canterbury'),
        ('Otago', 'Otago'),
        ('Southland', 'Southland'),
    ]

    #Location Filter
    location = django_filters.ChoiceFilter(field_name='location', lookup_expr='exact', choices=LOCATION_CHOICES)

    class Meta:
        model = Listing
        fields = ['category', 'price', 'location']