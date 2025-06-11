from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .models import Category, Dish, Promotion, Order, Contact, DeliveryInfo

# Create your views here.
class HomeView(TemplateView):
    template_name = 'fastfood/home.html'

class AboutView(TemplateView):
    template_name = 'fastfood/about.html'

class ContactsView(TemplateView):
    template_name = 'fastfood/contacts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        return context

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'fastfood/contact_detail.html'
    context_object_name = 'contact'

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'fastfood/contact_form.html'
    fields = ['address', 'phone', 'email']
    success_url = reverse_lazy('contacts')

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'fastfood/contact_form.html'
    fields = ['address', 'phone', 'email']
    success_url = reverse_lazy('contacts')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'fastfood/contact_confirm_delete.html'
    success_url = reverse_lazy('contacts')

class FindUsView(TemplateView):
    template_name = 'fastfood/find_us.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'fastfood/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'fastfood/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'fastfood/category_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'fastfood/category_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'fastfood/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

class DishListView(ListView):
    model = Dish
    template_name = 'fastfood/dish_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        if category_id:
            context['current_category'] = get_object_or_404(Category, pk=category_id)
        return context

class DishDetailView(DetailView):
    model = Dish
    template_name = 'fastfood/dish_detail.html'
    context_object_name = 'dish'

class DishCreateView(CreateView):
    model = Dish
    template_name = 'fastfood/dish_form.html'
    fields = ['name', 'category', 'price', 'description', 'image']
    success_url = reverse_lazy('dish_list')

class DishUpdateView(UpdateView):
    model = Dish
    template_name = 'fastfood/dish_form.html'
    fields = ['name', 'category', 'price', 'description', 'image']
    success_url = reverse_lazy('dish_list')

class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'fastfood/dish_confirm_delete.html'
    success_url = reverse_lazy('dish_list')

class CartView(TemplateView):
    template_name = 'fastfood/cart.html'

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

class CartAddView(View):
    def get(self, request, dish_id):
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

class CartRemoveView(View):
    def get(self, request, dish_id):
        cart = request.session.get('cart', {})
        if str(dish_id) in cart:
            del cart[str(dish_id)]
            request.session['cart'] = cart
            request.session.modified = True
        return redirect('cart')

class PromotionListView(ListView):
    model = Promotion
    template_name = 'fastfood/promotion_list.html'
    context_object_name = 'promotions'

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'fastfood/promotion_detail.html'
    context_object_name = 'promotion'

class PromotionCreateView(CreateView):
    model = Promotion
    template_name = 'fastfood/promotion_form.html'
    fields = ['title', 'description', 'image', 'start_date', 'end_date']
    success_url = reverse_lazy('promotion_list')

class PromotionUpdateView(UpdateView):
    model = Promotion
    template_name = 'fastfood/promotion_form.html'
    fields = ['title', 'description', 'image', 'start_date', 'end_date']
    success_url = reverse_lazy('promotion_list')

class PromotionDeleteView(DeleteView):
    model = Promotion
    template_name = 'fastfood/promotion_confirm_delete.html'
    success_url = reverse_lazy('promotion_list')

class OrderListView(ListView):
    model = Order
    template_name = 'fastfood/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'fastfood/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'fastfood/order_form.html'
    fields = ['customer_name', 'address', 'total_price']
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'fastfood/order_form.html'
    fields = ['customer_name', 'address', 'total_price']
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'fastfood/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

class DeliveryView(TemplateView):
    template_name = 'fastfood/delivery.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delivery_info'] = DeliveryInfo.objects.first()
        return context