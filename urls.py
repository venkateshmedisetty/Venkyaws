from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/thank-you/', views.contact_thank_you, name='contact_thank_you'),
    path('register/', views.vendor_register, name='vendor_register'),
    path('login/', views.vendor_login, name='vendor_login'),
    path('logout/', views.vendor_logout, name='vendor_logout'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:product_id>/pdf/', views.view_pdf, name='view_pdf'),
]
