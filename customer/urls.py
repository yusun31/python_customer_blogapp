from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list_home'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
]