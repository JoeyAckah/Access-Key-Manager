from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Accesskey

# Create your views here.

@login_required(login_url='account_login')
def index(request):
    keys = Accesskey.objects.filter()
    context = {
        'keys': keys,
    }
    return render(request, 'key_manager/index.html', context)

def signup(request):
    form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)