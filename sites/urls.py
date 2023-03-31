from django.urls import path
from . import views
from .views import registration_view, account_properties_view, update_account_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('sites', views.SiteList.as_view(), name='site_list'),
    path('sites/<int:pk>', views.SiteDetail.as_view(), name='site_detail'),
    
    
    path('register', registration_view, name='register'),
    path('properties', account_properties_view, name='properties'),
    path('properties/update', update_account_view, name='update'),
    path('login', obtain_auth_token, name='login'),
]