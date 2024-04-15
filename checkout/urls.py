from django.urls import path
from checkout import views

urlpatterns = [
    path('stripe', views.stripe_transaction, name='checkout.stripe'),
    path('paypal', views.paypal_transaction, name='checkout.paypal')
]
