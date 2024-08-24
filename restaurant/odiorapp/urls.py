from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('order-food/', views.order_placing, name='order'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('about-us/', views.about_us, name='about-us'),
    path('order-success/', views.order_success, name='order-success'),


    
]