from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('key-request', views.assign_key, name='key-request'),
    path('logout', views.logout, name='logout'),
    path('revoke/<int:id>', views.revoke, name='revoke'),
    path('api/key-check', views.check_key, name='check-active-key'),
    
]