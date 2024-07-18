from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Accesskey
from django.db.models import Q
from django.contrib import messages
from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import AccesskeySerializer





def logout(request):
    auth.logout(request)
    return redirect('account_login')

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def check_key(request, format=None):
        if request.method == 'POST':
            email = request.POST['email-search']
            try:
                user = User.objects.get(email=email)
                active_key = Accesskey.objects.filter(user=user, status='ACTIVE').first()

                if active_key:
                    serializer = AccesskeySerializer(active_key, many=False)
                    response = serializer.data
                    response['STATUS_CODE'] = status.HTTP_200_OK
                    return render(request, 'key_manager/api_response.html', {'response':response,'email':email})
                else:
                    response = {'detail':'This user has no active key','STATUS_CODE':status.HTTP_404_NOT_FOUND}
                    return render(request, 'key_manager/api_response.html', {'response':response,'email':email})
                

            except User.DoesNotExist:
                response = {'detail':'Email not found', 'STATUS_CODE':status.HTTP_404_NOT_FOUND}
                return render(request, 'key_manager/api_response.html', {'response': response,'email':email})

    



@login_required(login_url='account_login')
def index(request):
    has_keys = True if Accesskey.objects.filter(user=request.user).exists() else False
    q = request.GET.get('q') if request.method == 'GET' else ''
    if q:
        keys = Accesskey.objects.filter(Q(status__icontains=q), user=request.user) if not request.user.is_superuser else Accesskey.objects.filter(Q(status__icontains=q))
    else:
        try:
            active_key=Accesskey.objects.get(user=request.user, status='ACTIVE')
            if active_key:
                active_key.status = update_status(active_key)
                active_key.save()
        except Exception:
            keys = Accesskey.objects.filter(user=request.user)

        if request.user.is_superuser:
            keys = Accesskey.objects.all()
        else:
            keys = Accesskey.objects.filter(user=request.user)
    context = {
        'keys': keys,
        'has_keys': has_keys
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


