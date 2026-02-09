from django.contrib import admin
from django.urls import path
from products import views, api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("track-order/", views.order_tracking_page),
    path("api/orders/create/", api.create_order),
]
