from django.shortcuts import render, redirect
from .models import Product, Order

def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def dashboard(request):
    return render(request, "backend/dashboard.html")


def products(request):
    items = Product.objects.all()
    return render(request, "backend/products.html", {"products": items})


def add_product(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST["name"],
            price=request.POST["price"],
            description=request.POST["description"],
            image=request.FILES["image"],
        )
        return redirect("/backend/products/")
    return render(request, "backend/add_product.html")


def orders(request):
    all_orders = Order.objects.all()
    return render(request, "backend/orders.html", {"orders": all_orders})
