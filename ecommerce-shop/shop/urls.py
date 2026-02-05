from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    from products.views import create_order, track_order, order_tracking_page
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
        path('cart.html', TemplateView.as_view(template_name='cart.html'), name='cart'),
    path('checkout.html', TemplateView.as_view(template_name='checkout.html'), name='checkout'),
    path('bill.html', TemplateView.as_view(template_name='bill.html'), name='bill'),
        # Order Management API Endpoints
    path('api/create-order/', create_order, name='create-order'),
    path('api/track-order/<str:order_id>/', track_order, name='track-order'),
    path('order-tracking/', order_tracking_page, name='order-tracking'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
