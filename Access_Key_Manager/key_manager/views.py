from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def index(request):

    return render(request, 'key_manager/index.html')

def signup(request):
    form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)