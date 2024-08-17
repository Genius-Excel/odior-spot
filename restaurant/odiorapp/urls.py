from django.urls import path
from . import views


urlpatterns = [
    path('', views.sample, name='sample'),
    path('book-test/', views.book_test, name='book-test'),
    
]