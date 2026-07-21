from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='lambo.webp', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    price = models.FloatField()

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

    location = models.CharField(max_length=25, choices = LOCATION_CHOICES, null=True)

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

    category = models.CharField(max_length=25, choices = CATEGORY_CHOICES, null=True)
    
    def __str__(self):
        return self.title