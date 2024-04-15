import math

from django.shortcuts import redirect
from .models import Transaction
from .forms import UserInfoForm
from store.models import Product, Cart, Order
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import PaymentMethod

# Create your views here.
def stripe_transaction(request):
    transaction = make_transaction(request, PaymentMethod.Stripe)
def paypal_transaction(request):
    transaction = make_transaction(request, PaymentMethod.Paypal)
def make_transaction(request, pm):
    form = UserInfoForm(request.POST)
    if form.is_valid():
        cart = Cart.objects.filter(session=request.session.session_key).last()
        products = Product.objects.filter(pk__in=cart.items)

        total = 0
        for item in products:
            total += item.price
        if total <= 0:
            return None

        return Transaction.objects.create(
            customer=form.cleaned_data,
            session=request.session.session_key,
            pyment_method=pm,
            items=cart.items,
            amount=math.ceil(total)
        )

def send_order_email(order, products):
    msg_html = render_to_string('email/order.html', {
        'order': order,
        'products': products
    })
    send_mail(
        subject='New Order',
        html_message=msg_html,
        message=msg_html,
        from_email='aminekhalfaoui814@gmail.com',
        recipient_list=[order.customer['email']]
    )
