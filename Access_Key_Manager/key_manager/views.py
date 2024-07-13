from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import SignUpForm
from .models import Accesskey
from django.db.models import Q
from django.contrib import messages
from datetime import datetime, timedelta


# Create your views here.

@login_required(login_url='account_login')
def index(request):
    q = request.GET.get('q') if request.method == 'GET' else ''
    if q:
        keys = Accesskey.objects.filter(Q(status__icontains=q), user=request.user)
    else:
        try:
            active_key=Accesskey.objects.get(user=request.user, status='ACTIVE')
            if active_key:
                active_key.status = update_status(active_key)
                active_key.save()
        except Exception:
            keys = Accesskey.objects.filter(user=request.user)
            
        keys = Accesskey.objects.filter(user=request.user)
    context = {
        'keys': keys,
    }
    return render(request, 'key_manager/index.html', context)

def update_status(key):
        return 'EXPIRED' if datetime.now().date() >= key.expiry_date else 'ACTIVE'
            # key.status=key.status_choices['EXPIRED']
            
            

def assign_key(request):
    active_key = Accesskey.objects.filter(user=request.user, status='ACTIVE')
    if active_key:
        messages.info(request, 'You already have an active key!')
        return redirect('index')
    else:
        date_procured = datetime.now()
        new_key = Accesskey.objects.create(
            user = request.user,
            status = 'ACTIVE',
            date_procured = date_procured,
            expiry_date = date_procured + timedelta(days=365)

        )
        new_key.save()
        messages.success(request, 'You have a new key!')
        return redirect('index')
    

def revoke(request, id):
    key = Accesskey.objects.get(id=id)
    key.status = 'REVOKED'
    key.save()
    return redirect('index')


def signup(request):
    form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)