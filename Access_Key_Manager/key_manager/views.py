from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Accesskey
from django.db.models import Q
from django.contrib import messages
import datetime


# Create your views here.

@login_required(login_url='account_login')
def index(request):
    q = request.GET.get('q') if request.method == 'GET' else ''
    if q:
        keys = Accesskey.objects.filter(Q(status__icontains=q), user=request.user)
    else:
        keys = Accesskey.objects.filter(user=request.user)
    
    context = {
        'keys': keys,
    }
    return render(request, 'key_manager/index.html', context)


def assign_key(request):
    active_key = Accesskey.objects.filter(user=request.user, status='ACTIVE')
    if active_key:
        messages.info(request, 'You already have an active key!')
        return redirect('index')
    else:
        new_key = Accesskey.objects.create(
            user = request.user,
            status = 'ACTIVE',
            date_procured = datetime.datetime.now(),
            expiry_date = datetime.datetime.now(),

        )
        new_key.save()
        messages.success(request, 'You have a new key!')
        return redirect('index')
    


def signup(request):
    form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)