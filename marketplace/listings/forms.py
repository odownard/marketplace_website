from django import forms
from . import models

class CreateListing(forms.ModelForm):
    class Meta:
        model = models.Listing
        fields = ['title', 'body', 'banner', 'price', 'location', 'category']

        widgets ={
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Name of Listing'
            }),
            'category': forms.Select(attrs={
                'class': 'form-input',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Description'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Price'
            }),
            'banner': forms.FileInput(attrs={
                'class': 'form-input'
            })
        }