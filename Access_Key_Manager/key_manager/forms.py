from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm


class CustomSignUpForm(SignupForm):
    username = forms.CharField(max_length=255, label='Username', required=True, widget=forms.TextInput(attrs={
        'id': 'username'
    }))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={
        'id': 'email'
    }))
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={
        'id': 'password'
    }))
    password2 = forms.CharField(label='Confirm Password', required=True, widget=forms.PasswordInput(attrs={
        'id': 'confirm-password'
    }))

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.save()
        return user
    