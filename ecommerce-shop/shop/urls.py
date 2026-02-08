from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from products import api

urlpatterns = [
    # ✅ Django Admin (DO NOT TOUCH)
    path("admin/", admin.site.urls),

    # ✅ Website pages
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("cart.html", TemplateView.as_view(template_name="cart.html"), name="cart"),
    path("checkout.html", TemplateView.as_view(template_name="checkout.html"), name="checkout"),
    path("bill.html", TemplateView.as_view(template_name="bill.html"), name="bill"),

    # ✅ API Endpoints
    path("api/orders/", api.get_all_orders),
    path("api/orders/<str:order_id>/", api.get_order_by_id),
    path("api/orders/status/<str:status>/", api.get_orders_by_status),
    path("api/orders/<str:order_id>/update-status/", api.update_order_status),
    path("api/orders/statistics/", api.get_order_statistics),
]

# Static & media
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
