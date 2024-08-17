from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderRequest
from .forms import OrderRequestForm
from django.contrib import messages

# Create your views here.

def sample(request):
    return render(request, 'odiorapp/sample.html')


def book_test(request):
    form = OrderRequestForm()
    if request.method == "POST":
        form = OrderRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Favour you are a Genius. Forget about the motherfucking recruiters")
        else:
            messages.error(request, "An error occured.")
    else:
        form = OrderRequestForm()

    context = {"form": form}
    return render(request, 'odiorapp/book-test.html', context)
