from django.urls import path
from checkout import views

urlpatterns = [
    path('order', views.make_order, name='checkout.order')
]
