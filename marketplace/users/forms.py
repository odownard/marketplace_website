from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

# class CustomRegistrationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = User
#         fields = ('username', 'password')
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': 'Username'}),
#             'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
#         }

class CustomLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control' # Optional: Add CSS classes
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))