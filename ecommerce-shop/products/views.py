from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from .models import Order, OrderItem, Product


@csrf_exempt
@require_http_methods(["POST"])
def create_order(request):
    """
    API endpoint to create a new order from checkout form data
    Expected POST data: {
        'order_id': str,
        'customer_name': str,
        'customer_email': str,
        'customer_phone': str,
        'customer_address': str,
        'customer_city': str,
        'customer_state': str,
        'customer_pincode': str,
        'customer_country': str,
        'items': [{'product_id': int, 'quantity': int, 'price': float}],
        'subtotal': float,
        'tax': float,
        'shipping_cost': float,
        'total_amount': float,
        'payment_method': str
    }
    """
    try:
        data = json.loads(request.body)
        
        # Create Order
        order = Order.objects.create(
            order_id=data.get('order_id'),
            customer_name=data.get('customer_name'),
            customer_email=data.get('customer_email'),
            customer_phone=data.get('customer_phone'),
            customer_address=data.get('customer_address'),
            customer_city=data.get('customer_city'),
            customer_state=data.get('customer_state'),
            customer_pincode=data.get('customer_pincode'),
            customer_country=data.get('customer_country', 'India'),
            subtotal=data.get('subtotal', 0),
            tax=data.get('tax', 0),
            shipping_cost=data.get('shipping_cost', 50),
            total_amount=data.get('total_amount', 0),
            payment_method=data.get('payment_method', 'cod'),
            status='pending'
        )
        
        # Create OrderItems
        items_data = data.get('items', [])
        for item in items_data:
            product = Product.objects.get(id=item.get('product_id'))
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item.get('quantity', 1),
                price_at_purchase=item.get('price', product.price)
            )
        
        return JsonResponse({
            'success': True,
            'order_id': order.order_id,
            'message': 'Order created successfully'
        })
    
    except Product.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Product not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


@require_http_methods(["GET"])
def track_order(request, order_id):
    """
    API endpoint to track order status
    Returns order details and items
    """
    try:
        order = get_object_or_404(Order, order_id=order_id)
        items = order.items.all()
        
        items_data = [{
            'product': item.product.name,
            'quantity': item.quantity,
            'price': str(item.price_at_purchase),
            'total': str(item.get_item_total())
        } for item in items]
        
        return JsonResponse({
            'order_id': order.order_id,
            'status': order.status,
            'customer_name': order.customer_name,
            'customer_email': order.customer_email,
            'total_amount': str(order.total_amount),
            'payment_method': order.payment_method,
            'created_at': order.created_at.isoformat(),
            'items': items_data
        })
    
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def order_tracking_page(request):
    """
    Page for customers to track their orders
    """
    return render(request, 'order-tracking.html')
def product_list(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'products.html', {'products': products})
