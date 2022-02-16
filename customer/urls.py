from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list_home'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customer/new/', views.customer_new, name='customer_new'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/remove/', views.customer_remove, name='customer_remove'),
    path('customer/<int:pk>/comment/', views.add_comment_to_customer, name='add_comment_to_customer'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]