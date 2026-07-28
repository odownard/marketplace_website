from django import forms
from . import models

class CreateListing(forms.ModelForm):
    class Meta:
        model = models.Listing
        fields = ['title', 'body', 'banner', 'price', 'location', 'category']