from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2', )
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-6 py-4 rounded-xl',
        'placeholder': 'Your username'
        }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'w-full px-6 py-4 rounded-xl',
        'placeholder': 'Your email'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-6 py-4 rounded-xl',
        'placeholder': 'Your password'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-6 py-4 rounded-xl',
        'placeholder': 'Confirm your password'
        }))