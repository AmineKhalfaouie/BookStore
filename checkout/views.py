from django.shortcuts import redirect
from .forms import UserInfoForm
from store.models import Product, Cart, Order

# Create your views here.
def make_order(request):
    if request.method != 'POST':
        return redirect('store.checkout')
    form = UserInfoForm(request.POST)
    if form.is_valid():
        cart = Cart.objects.filter(session=request.session.session_key).last()
        products = Product.objects.filter(pk__in=cart.items)

        total = 0
        for item in products:
            total += item.price
        if total <= 0:
            return redirect('store.cart')

        order = Order.objects.create(customer=form.cleaned_data, total=total)
        for product in products:
            order.orderproduct_set.create(product_id=product.id, price=product.price)

        cart.delete()
        return redirect('store.checkout_complete')
    else:
        return redirect('store.checkout')
