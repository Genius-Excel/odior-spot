from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import OrderRequest
from .forms import OrderRequestForm
from django.contrib import messages

# Create your views here.

def home(request):
    context = {'title': 'Home', 'page': 'home'}
    return render(request, 'odiorapp/home.html', context)


def contact_us(request):
    context = {'title': 'Contact Us', 'page': 'contact-us'}
    return render(request, 'odiorapp/contact-us.html', context)


def about_us(request):
    context = {'title': 'About Us', 'page': 'about-us'}
    return render(request, 'odiorapp/about-us.html', context)


def order_success(request):
    context = {'title': 'Successful Order'}
    return render(request, 'odiorapp/order-success.html', context)

def order_placing(request):
    form = OrderRequestForm()
    if request.method == "POST":
        form = OrderRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-success')
        else:
            messages.error(request, "An error occured.")
    else:
        form = OrderRequestForm()

    context = {"form": form, "page": 'order'}
    return render(request, 'odiorapp/order.html', context)
