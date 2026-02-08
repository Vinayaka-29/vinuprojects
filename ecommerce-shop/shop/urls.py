from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from products import backend_views
from products import api

urlpatterns = [
    # ✅ Django Admin (DO NOT OVERRIDE)
    path('admin/', admin.site.urls),

    # ✅ Website pages
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('cart.html', TemplateView.as_view(template_name='cart.html'), name='cart'),
    path('checkout.html', TemplateView.as_view(template_name='checkout.html'), name='checkout'),
    path('bill.html', TemplateView.as_view(template_name='bill.html'), name='bill'),

    # ✅ Custom Admin Backend (NOT Django admin)
    path('dashboard/', backend_views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/orders/', backend_views.view_all_orders, name='view_all_orders'),
    path('dashboard/orders/<str:order_id>/', backend_views.view_order_detail, name='view_order_detail'),
    path('dashboard/reports/', backend_views.reports, name='admin_reports'),
    path('dashboard/orders/export-csv/', backend_views.export_orders_csv, name='export_orders_csv'),
    path(
        'dashboard/orders/<str:order_id>/update-status/',
        backend_views.update_order_status,
        name='update_order_status_view'
    ),

    # ✅ API Endpoints
    path('api/orders/', api.get_all_orders, name='api_get_all_orders'),
    path('api/orders/<str:order_id>/', api.get_order_by_id, name='api_get_order_detail'),
    path('api/orders/status/<str:status>/', api.get_orders_by_status, name='api_get_orders_by_status'),
    path('api/orders/<str:order_id>/update-status/', api.update_order_status, name='api_update_order_status'),
    path('api/orders/statistics/', api.get_order_statistics, name='api_get_statistics'),
]

# ✅ Static & Media (Render + local)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
