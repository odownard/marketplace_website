from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
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

    location = models.CharField(choices = LOCATION_CHOICES, null=True)
    
    def __str__(self):
        return self.title