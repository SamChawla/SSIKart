from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def home(request):
    products = Product.objects.filter(is_available=True)

    context_data = {
        "products" : products,
    }

    return render(request, "home.html", context_data)


def about(request):
    return HttpResponse("<h1> Django E-Commerce Project by Sumit Chawla </h1>")


