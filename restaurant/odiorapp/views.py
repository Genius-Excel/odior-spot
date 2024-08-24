from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import OrderRequest
from .forms import OrderRequestForm
from django.contrib import messages
from django.conf import settings
import mailtrap as mt
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import socket

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
            customer_name = form.cleaned_data['customer_name']
            order_item = form.cleaned_data['order_item']
            order_quantity = form.cleaned_data['order_quantity']
            special_request = form.cleaned_data['special_request']
            email = form.cleaned_data['email']
            # Catch any error while trying to send confirmation email.
            try:
                template_loader = FileSystemLoader(searchpath=Path(__file__).parent)
                template_env = Environment(loader=template_loader)
                template_file = 'templates/odiorapp/order-confirmation.html'
                template_file_content = template_env.get_template(template_file)

                template_context = {
                    'customer_name': customer_name,
                    'order_item': order_item,
                    'order_quantity': order_quantity,
                    'special_request': special_request,
                    'email': email,
                }

                # embbed context variables in HTML
                html_content = template_file_content.render(template_context)

                # send Employee mail via mailtrap.
                mail = mt.Mail(
                    sender=mt.Address(email='noreply@easyappz.com', name="Odiorspot Kitchen"),
                    to=[mt.Address(email=email)],
                    subject='Order Request Confirmation',
                    text=None,
                    html=html_content,
                )

                client = mt.MailtrapClient(token=settings.SMTP_API_TOKEN)
                client.send(mail)

                form.save()
                messages.success(request, f"Email has been sent successfuly to {email}")
                return redirect('order-success')
            except socket.gaierror:
                messages.error(request, 'An error occured while trying place an order, kindly check your internet connection.')
            except Exception as e:
                messages.error(request, f"Error {e} occured. Please check your internet connection.")
        else:
            messages.error(request, "An error occured with the form.")
    else:
        form = OrderRequestForm()

    context = {"form": form, "page": 'order'}
    return render(request, 'odiorapp/order.html', context)
