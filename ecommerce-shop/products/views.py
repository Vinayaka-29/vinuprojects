from django.shortcuts import render
from .models import Product, Order

def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def order_detail(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        return render(request, "order_detail.html", {"order": order})
    except Order.DoesNotExist:
        return render(request, "order_not_found.html")
