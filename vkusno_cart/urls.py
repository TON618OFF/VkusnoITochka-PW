from django.urls import path
from .views import CartView, CartAddView, CartRemoveView, CartUpdateView, OrderCreateFromCartView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add/<int:dish_id>/', CartAddView.as_view(), name='cart_add'),
    path('remove/<int:dish_id>/', CartRemoveView.as_view(), name='cart_remove'),
    path('update/<int:dish_id>/', CartUpdateView.as_view(), name='cart_update'),
    path('order/', OrderCreateFromCartView.as_view(), name='order_create_from_cart'),
]