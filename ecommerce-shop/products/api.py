from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from functools import wraps
import json
from .models import Order, OrderItem

# =======================
# ADMIN API AUTHENTICATION
# =======================

def token_auth_required(f):
    """Decorator for API endpoints requiring admin token authentication"""
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        
        if not auth_header.startswith('Bearer '):
            return JsonResponse({
                'success': False,
                'error': 'Missing or invalid authorization header. Use: Authorization: Bearer <token>'
            }, status=401)
        
        token = auth_header.split(' ')[1]
        # For vinayaka29 user, token should be pre-configured
        VALID_TOKEN = 'vinayaka29_admin_token_2024'
        
        if token != VALID_TOKEN:
            return JsonResponse({
                'success': False,
                'error': 'Invalid authentication token'
            }, status=403)
        
        return f(request, *args, **kwargs)
    return decorated_function

# =======================
# ADMIN ORDER MANAGEMENT API
# =======================

@token_auth_required
@require_http_methods(["GET"])
def get_all_orders(request):
    """
    API endpoint to retrieve all orders from the website
    Requires: Authorization: Bearer <token> header
    Returns: List of all orders with details
    """
    try:
        orders = Order.objects.all().order_by('-created_at')
        
        orders_data = []
        for order in orders:
            items = order.items.all()
            items_data = [{
                'product_name': item.product.name,
                'quantity': item.quantity,
                'price_at_purchase': str(item.price_at_purchase),
                'item_total': str(item.get_item_total())
            } for item in items]
            
            orders_data.append({
                'id': order.id,
                'order_id': order.order_id,
                'customer_name': order.customer_name,
                'customer_email': order.customer_email,
                'customer_phone': order.customer_phone,
                'customer_address': order.customer_address,
                'customer_city': order.customer_city,
                'customer_state': order.customer_state,
                'customer_pincode': order.customer_pincode,
                'customer_country': order.customer_country,
                'subtotal': str(order.subtotal),
                'tax': str(order.tax),
                'shipping_cost': str(order.shipping_cost),
                'total_amount': str(order.total_amount),
                'payment_method': order.payment_method,
                'status': order.status,
                'created_at': order.created_at.isoformat(),
                'updated_at': order.updated_at.isoformat(),
                'items': items_data
            })
        
        return JsonResponse({
            'success': True,
            'total_orders': len(orders_data),
            'orders': orders_data
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


@token_auth_required
@require_http_methods(["GET"])
def get_order_by_id(request, order_id):
    """
    API endpoint to retrieve a specific order by order_id
    Requires: Authorization: Bearer <token> header
    """
    try:
        order = Order.objects.get(order_id=order_id)
        items = order.items.all()
        
        items_data = [{
            'product_name': item.product.name,
            'quantity': item.quantity,
            'price_at_purchase': str(item.price_at_purchase),
            'item_total': str(item.get_item_total())
        } for item in items]
        
        return JsonResponse({
            'success': True,
            'order': {
                'id': order.id,
                'order_id': order.order_id,
                'customer_name': order.customer_name,
                'customer_email': order.customer_email,
                'customer_phone': order.customer_phone,
                'customer_address': order.customer_address,
                'customer_city': order.customer_city,
                'customer_state': order.customer_state,
                'customer_pincode': order.customer_pincode,
                'customer_country': order.customer_country,
                'subtotal': str(order.subtotal),
                'tax': str(order.tax),
                'shipping_cost': str(order.shipping_cost),
                'total_amount': str(order.total_amount),
                'payment_method': order.payment_method,
                'status': order.status,
                'created_at': order.created_at.isoformat(),
                'updated_at': order.updated_at.isoformat(),
                'items': items_data
            }
        })
    
    except Order.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Order not found'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


@token_auth_required
@require_http_methods(["GET"])
def get_orders_by_status(request, status):
    """
    API endpoint to retrieve orders filtered by status
    Statuses: pending, confirmed, shipped, delivered, cancelled
    Requires: Authorization: Bearer <token> header
    """
    valid_statuses = ['pending', 'confirmed', 'shipped', 'delivered', 'cancelled']
    
    if status not in valid_statuses:
        return JsonResponse({
            'success': False,
            'error': f'Invalid status. Valid statuses: {valid_statuses}'
        }, status=400)
    
    try:
        orders = Order.objects.filter(status=status).order_by('-created_at')
        
        orders_data = []
        for order in orders:
            items = order.items.all()
            items_data = [{
                'product_name': item.product.name,
                'quantity': item.quantity,
                'price_at_purchase': str(item.price_at_purchase),
                'item_total': str(item.get_item_total())
            } for item in items]
            
            orders_data.append({
                'id': order.id,
                'order_id': order.order_id,
                'customer_name': order.customer_name,
                'customer_email': order.customer_email,
                'total_amount': str(order.total_amount),
                'payment_method': order.payment_method,
                'status': order.status,
                'created_at': order.created_at.isoformat(),
                'items': items_data
            })
        
        return JsonResponse({
            'success': True,
            'status_filter': status,
            'total_orders': len(orders_data),
            'orders': orders_data
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


@token_auth_required
@require_http_methods(["POST"])
def update_order_status(request, order_id):
    """
    API endpoint to update order status
    Expected POST data: {'status': 'confirmed|shipped|delivered|cancelled'}
    Requires: Authorization: Bearer <token> header
    """
    try:
        data = json.loads(request.body)
        new_status = data.get('status')
        
        valid_statuses = ['pending', 'confirmed', 'shipped', 'delivered', 'cancelled']
        if not new_status or new_status not in valid_statuses:
            return JsonResponse({
                'success': False,
                'error': f'Invalid status. Valid statuses: {valid_statuses}'
            }, status=400)
        
        order = Order.objects.get(order_id=order_id)
        order.status = new_status
        order.save()
        
        return JsonResponse({
            'success': True,
            'message': f'Order {order_id} status updated to {new_status}',
            'order_id': order.order_id,
            'new_status': order.status
        })
    
    except Order.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Order not found'
        }, status=404)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


@token_auth_required
@require_http_methods(["GET"])
def get_order_statistics(request):
    """
    API endpoint to get order statistics for admin dashboard
    Returns: Total orders, total revenue, orders by status
    Requires: Authorization: Bearer <token> header
    """
    try:
        all_orders = Order.objects.all()
        total_orders = all_orders.count()
        total_revenue = sum(order.total_amount for order in all_orders)
        
        status_breakdown = {}
        for status, _ in Order.ORDER_STATUS_CHOICES:
            count = all_orders.filter(status=status).count()
            status_breakdown[status] = count
        
        # Payment method breakdown
        payment_breakdown = {}
        for method, _ in Order.PAYMENT_METHOD_CHOICES:
            count = all_orders.filter(payment_method=method).count()
            payment_breakdown[method] = count
        
        return JsonResponse({
            'success': True,
            'statistics': {
                'total_orders': total_orders,
                'total_revenue': str(total_revenue),
                'status_breakdown': status_breakdown,
                'payment_method_breakdown': payment_breakdown
            }
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
