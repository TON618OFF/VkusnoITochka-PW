from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from fastfood.models import Dish, Order, OrderItem, Delivery, UserProfile
from fastfood.forms import OrderForm

class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'vkusno_cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        cart_items = []
        total_price = 0

        for dish_id, item in cart.items():
            dish = get_object_or_404(Dish, pk=dish_id)
            item_total = item['quantity'] * item['price']
            cart_items.append({
                'dish': dish,
                'quantity': item['quantity'],
                'price': item['price'],
                'total_price': item_total
            })
            total_price += item_total

        context['cart'] = cart_items
        context['total_price'] = total_price
        return context

class CartAddView(LoginRequiredMixin, View):
    def post(self, request, dish_id):
        dish = get_object_or_404(Dish, pk=dish_id)
        cart = request.session.get('cart', {})
        
        if str(dish_id) in cart:
            cart[str(dish_id)]['quantity'] += 1
        else:
            cart[str(dish_id)] = {
                'quantity': 1,
                'price': float(dish.price)
            }
        
        request.session['cart'] = cart
        request.session.modified = True
        return redirect('cart')

class CartRemoveView(LoginRequiredMixin, View):
    def post(self, request, dish_id):
        cart = request.session.get('cart', {})
        if str(dish_id) in cart:
            del cart[str(dish_id)]
            request.session['cart'] = cart
            request.session.modified = True
        return redirect('cart')

class CartUpdateView(LoginRequiredMixin, View):
    def post(self, request, dish_id):
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get('quantity', 1))
        if str(dish_id) in cart:
            if quantity > 0:
                cart[str(dish_id)]['quantity'] = quantity
            else:
                del cart[str(dish_id)]
            request.session['cart'] = cart
            request.session.modified = True
        return redirect('cart')

class OrderCreateFromCartView(LoginRequiredMixin, View):
    def get(self, request):
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart')
        profile = get_object_or_404(UserProfile, user=request.user)
        initial_data = {
            'last_name': profile.last_name,
            'first_name': profile.first_name,
            'patronymic': profile.patronymic,
            'phone': profile.phone,
            'email': request.user.email,
            'address': profile.address,
        }
        form = OrderForm(initial=initial_data)
        return render(request, 'vkusno_cart/order_create.html', {'form': form})

    def post(self, request):
        form = OrderForm(request.POST)
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart')
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = sum(item['quantity'] * item['price'] for item in cart.values())
            order.save()
            for dish_id, item in cart.items():
                dish = get_object_or_404(Dish, pk=dish_id)
                OrderItem.objects.create(
                    order=order,
                    dish=dish,
                    quantity=item['quantity']
                )
            if order.delivery_type == 'courier':
                Delivery.objects.create(order=order)
            request.session['cart'] = {}
            request.session.modified = True
            return redirect('profile')
        return render(request, 'vkusno_cart/order_create.html', {'form': form})