from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from django.views.decorators.http import require_POST
from .models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt



def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Subscriber.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Thank you for subscribing!'}, status=400)
        try:
            subscriber = Subscriber.objects.create(email=email)
            subscriber.save()
            return JsonResponse({'message': 'Thank you for subscribing!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=405)




@csrf_exempt
def updateItem(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        productId = data.get('productId')
        action = data.get('action')
        if not productId or not action:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        print('Action:', action)
        print('Product:', productId)

        # Get or create a guest customer ID
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        customer, created = Customer.objects.get_or_create(session_key=session_key)
        if created:
            customer.name = "Guest"
            customer.save()

        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        if action == 'add':
            orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
            if not created:
                return JsonResponse({'error': 'Product already in cart'}, status=400)
        elif action == 'remove':
            orderItem = OrderItem.objects.get(order=order, product=product)
            orderItem.delete()

        cart_items = order.get_cart_items

        return JsonResponse({'cartItems': cart_items}, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def productDetail(request, pk):
    product = Product.objects.get(id=pk)
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'product': product, 'cartItems': cartItems}
    return render(request, 'store/product_detail.html', context)



def login(request):
    context = {}
    return render(request, 'store/login-register.html', context)



def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)



def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)



def checkout(request):
    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)



def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    # Use the `get_user` function to properly evaluate the user
    from django.contrib.auth import get_user
    user = get_user(request)

    if user.is_anonymous:
        return JsonResponse({'error': 'User not found'}, status=400)
    
    try:
        customer = user.customer
    except Customer.DoesNotExist:
        customer = Customer.objects.create(user=user, name=user.username, email=user.email)

    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    if action == 'add':
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        if not created:
            return JsonResponse({'error': 'Product already in cart'}, status=400)
    elif action == 'remove':
        orderItem = OrderItem.objects.get(order=order, product=product)
        orderItem.delete()

    cart_items = order.get_cart_items

    return JsonResponse({'cartItems': cart_items}, safe=False)




def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)

def privacy_policy(request):
    return render(request, 'store/privacy_policy.html')

def about(request):
    return render(request, 'store/about.html')

