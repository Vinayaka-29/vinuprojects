from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from products import api

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", TemplateView.as_view(template_name="index.html")),
    path("cart.html", TemplateView.as_view(template_name="cart.html")),
    path("checkout.html", TemplateView.as_view(template_name="checkout.html")),
    path("bill.html", TemplateView.as_view(template_name="bill.html")),

    path("api/orders/create/", api.create_order),
    path("api/orders/<str:order_id>/", api.get_order_by_id),
]
