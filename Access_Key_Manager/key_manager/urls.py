from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('key-request', views.assign_key, name='key-request'),
    path('revoke/<int:id>', views.revoke, name='revoke'),
    path('signup', views.signup, name='account_signup'),
]