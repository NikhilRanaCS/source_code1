from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service1/', views.service1_view, name='service1'),
    path('AKTU_ONE_SHOT/', views.AKTU_ONE_SHOT, name='AKTU_ONE_SHOT'),
     path('previous/', views.previous, name='previous'),
     path('mini', views.mini, name='mini'),
    path('service2/', views.service2_view, name='service2'),
    path('submit/', views.submit_data, name='submit'),
    path('success/', views.success_view, name='success'),
    path('download_zip/<int:option_selected>/', views.download_zip, name='download_zip'),
    path('payment/success/', views.payment_success, name='payment_success')
    # Add other URL patterns as needed
]
