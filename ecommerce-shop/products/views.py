from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def order_tracking_page(request):
    return render(request, "order-tracking.html")
