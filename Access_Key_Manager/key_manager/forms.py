from django import forms

from allauth.account.forms import SignupForm, LoginForm


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
    

class CustomLoginForm(LoginForm):
        login = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'id': 'email'}))
        password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'id':'password'}))
        remember = forms.BooleanField(label='Remember Me', required=False, widget=forms.CheckboxInput(attrs={'id':'remember-me'}))