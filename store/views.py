from django.shortcuts import render
from .models import Product, Slider

def index(request):
    products = Product.objects.select_related('author').filter(featured=True)
    slides = Slider.objects.order_by('order')

    return render(request, 'index.html', {
        'products': products,
        'slides': slides
    })

def product(request, pid):
    return render(request, 'product.html')
def category(request, cid):
    return render(request, 'category.html')
def cart(request):
    return render(request, 'cart.html')
def checkout(request):
    return render(request, 'checkout.html')
def checkout_complete(request):
    return render(request, 'checkout-complete.html')
