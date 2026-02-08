from django.contrib import admin
from .models import Category, Product, Order, OrderItem


# ----------------------
# CATEGORY ADMIN
# ----------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


# ----------------------
# PRODUCT ADMIN
# ----------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock_quantity", "is_available")
    list_filter = ("is_available",)
    search_fields = ("name",)


# ----------------------
# ORDER ITEM INLINE
# ----------------------
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product", "quantity", "price_at_purchase")


# ----------------------
# ORDER ADMIN
# ----------------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "customer_name", "total_amount", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("order_id", "customer_name", "customer_email")
    inlines = [OrderItemInline]


# ----------------------
# ORDER ITEM ADMIN
# ----------------------
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity", "price_at_purchase")
