from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Order
from .forms import OrderForm
from products_app.models import Product


# Create Order
@login_required
def create_order(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)
            order.user = request.user
            order.product = product
            order.save()

            messages.success(request, f'Order placed for "{product.product_name}"!')
            return redirect('order_list')

    else:
        form = OrderForm()

    return render(request, 'orders_app/create_order.html', {
        'form': form,
        'product': product
    })


# Order List — users see only their own; admin sees all
@login_required
def order_list(request):

    if request.user.is_staff:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)

    return render(request, 'orders_app/order_list.html', {
        'orders': orders
    })


# Delete Order
@login_required
def delete_order(request, id):

    order = get_object_or_404(Order, id=id)

    # Allow owner or admin to delete
    if order.user != request.user and not request.user.is_staff:
        messages.error(request, 'You cannot delete this order.')
        return redirect('order_list')

    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order cancelled.')
        return redirect('order_list')

    return render(request, 'orders_app/delete.html', {'order': order})
