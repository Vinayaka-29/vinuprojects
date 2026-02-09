from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from functools import wraps
import json

from .models import Order, OrderItem, Product


# =======================
# ADMIN TOKEN AUTH
# =======================

def token_auth_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.META.get("HTTP_AUTHORIZATION", "")

        if not auth_header.startswith("Bearer "):
            return JsonResponse(
                {"success": False, "error": "Authorization header missing"},
                status=401
            )

        token = auth_header.split(" ")[1]
        VALID_TOKEN = "vinayaka29_admin_token_2024"

        if token != VALID_TOKEN:
            return JsonResponse(
                {"success": False, "error": "Invalid token"},
                status=403
            )

        return view_func(request, *args, **kwargs)

    return wrapper


# =======================
# ADMIN APIs
# =======================

@token_auth_required
@require_http_methods(["GET"])
def get_all_orders(request):
    orders = Order.objects.all().order_by("-created_at")

    data = []
    for order in orders:
        items = [
            {
                "product": item.product.name,
                "quantity": item.quantity,
                "price": str(item.price_at_purchase),
                "total": str(item.get_item_total()),
            }
            for item in order.items.all()
        ]

        data.append({
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "customer_email": order.customer_email,
            "customer_phone": order.customer_phone,
            "customer_address": order.customer_address,
            "total_amount": str(order.total_amount),
            "status": order.status,
            "created_at": order.created_at.isoformat(),
            "items": items,
        })

    return JsonResponse({"success": True, "orders": data})


@token_auth_required
@require_http_methods(["GET"])
def get_order_by_id(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)
    except Order.DoesNotExist:
        return JsonResponse({"success": False, "error": "Order not found"}, status=404)

    items = [
        {
            "product": item.product.name,
            "quantity": item.quantity,
            "price": str(item.price_at_purchase),
            "total": str(item.get_item_total()),
        }
        for item in order.items.all()
    ]

    return JsonResponse({
        "success": True,
        "order": {
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "customer_email": order.customer_email,
            "customer_phone": order.customer_phone,
            "customer_address": order.customer_address,
            "total_amount": str(order.total_amount),
            "status": order.status,
            "created_at": order.created_at.isoformat(),
            "items": items,
        }
    })


@token_auth_required
@require_http_methods(["POST"])
def update_order_status(request, order_id):
    try:
        data = json.loads(request.body)
        new_status = data.get("status")

        if new_status not in ["pending", "confirmed", "shipped", "delivered", "cancelled"]:
            return JsonResponse({"success": False, "error": "Invalid status"}, status=400)

        order = Order.objects.get(order_id=order_id)
        order.status = new_status
        order.save()

        return JsonResponse({
            "success": True,
            "message": f"Order {order_id} updated to {new_status}"
        })

    except Order.DoesNotExist:
        return JsonResponse({"success": False, "error": "Order not found"}, status=404)

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


# =======================
# CUSTOMER APIs
# =======================

@csrf_exempt
@require_http_methods(["POST"])
def create_order(request):
    """
    Creates order from frontend checkout
    """
    try:
        data = json.loads(request.body)

        order = Order.objects.create(
            order_id=data["order_id"],
            customer_name=data["customer_name"],
            customer_email=data["customer_email"],
            customer_phone=data["customer_phone"],
            customer_address=data["customer_address"],
            total_amount=data["total_amount"],
            status="pending",
        )

        for item in data.get("items", []):
            product = Product.objects.get(id=item["product_id"])
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item["quantity"],
                price_at_purchase=item["price"],
            )

        return JsonResponse({
            "success": True,
            "order_id": order.order_id
        })

    except Product.DoesNotExist:
        return JsonResponse({"success": False, "error": "Product not found"}, status=404)

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


@require_http_methods(["GET"])
def track_order(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)

        items = [
            {
                "product": item.product.name,
                "quantity": item.quantity,
                "total": str(item.get_item_total()),
            }
            for item in order.items.all()
        ]

        return JsonResponse({
            "order_id": order.order_id,
            "status": order.status,
            "total_amount": str(order.total_amount),
            "items": items,
        })

    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)
