from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import CartItem
from products_app.models import Product
from orders_app.models import Order


# View cart
@login_required
def cart_view(request):

    cart_items = CartItem.objects.filter(user=request.user)

    # Calculate grand total
    total = sum(item.subtotal for item in cart_items)

    return render(request, 'cart_app/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


# Add to cart (max 2 different products allowed)
@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    # Check how many different products are already in cart
    current_count = CartItem.objects.filter(user=request.user).count()

    # Check if this product is already in cart
    existing = CartItem.objects.filter(user=request.user, product=product).first()

    if existing:
        # Product already in cart — just increase quantity
        existing.quantity += 1
        existing.save()
        messages.success(request, f'Updated quantity for "{product.product_name}" in cart.')

    elif current_count >= 2:
        # Cart already has 2 different products
        messages.warning(request, 'Cart is full. You can only add 2 different products at a time.')

    else:
        # Add new product to cart
        CartItem.objects.create(user=request.user, product=product, quantity=1)
        messages.success(request, f'"{product.product_name}" added to cart!')

    return redirect('cart_view')


# Remove one item from cart
@login_required
def remove_from_cart(request, item_id):

    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    name = item.product.product_name
    item.delete()
    messages.success(request, f'"{name}" removed from cart.')

    return redirect('cart_view')


# Checkout — create one order per cart item, then clear cart
@login_required
def checkout(request):

    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.warning(request, 'Your cart is empty!')
        return redirect('cart_view')

    # Create an Order for each cart item
    for item in cart_items:
        Order.objects.create(
            user=request.user,
            product=item.product,
            quantity=item.quantity
        )

    # Clear the cart after checkout
    cart_items.delete()

    messages.success(request, 'Order placed successfully! Check your orders.')
    return redirect('order_list')
