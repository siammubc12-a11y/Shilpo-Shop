from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Payment
from .forms import PaymentForm

from orders_app.models import Order


# Create Payment

@login_required
def payment_create(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    # Guard: if a payment already exists for this order, redirect away
    if Payment.objects.filter(order=order).exists():
        messages.warning(request, 'This order has already been paid.')
        return redirect('payment_list')

    if request.method == 'POST':

        form = PaymentForm(request.POST)

        if form.is_valid():

            payment = form.save(commit=False)

            payment.order = order
            payment.amount = order.total_price
            payment.payment_status = 'Completed'   # FIX 1: mark payment as Completed
            payment.save()

            # FIX 2: update order status so it no longer shows "Pending"
            order.status = 'Processing'
            order.save()

            messages.success(request, 'Payment successful!')
            return redirect('payment_list')

    else:

        form = PaymentForm()

    return render(request, 'payments_app/payment_form.html', {
        'form': form,
        'order': order
    })


# Payment List

def payment_list(request):

    payments = Payment.objects.all()

    return render(request, 'payments_app/payment_list.html', {
        'payments': payments
    })


# Delete Payment

def delete_payment(request, id):

    payment = get_object_or_404(Payment, id=id)

    if request.method == 'POST':

        payment.delete()

        return redirect('payment_list')

    return render(request, 'payments_app/delete.html', {
        'payment': payment
    })