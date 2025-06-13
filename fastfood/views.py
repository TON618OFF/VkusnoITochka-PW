from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from .models import Category, Dish, Promotion, Order, Contact, Delivery, UserProfile
from .forms import UserRegistrationForm, UserProfileForm, UserLoginForm, ContactForm, CategoryForm, DishForm, PromotionForm, OrderForm

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class HomeView(TemplateView):
    template_name = 'fastfood/home.html'

class AboutView(TemplateView):
    template_name = 'fastfood/about.html'

class ContactsView(ListView):
    model = Contact
    template_name = 'fastfood/contacts.html'
    context_object_name = 'contacts'

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'fastfood/contact_detail.html'
    context_object_name = 'contact'

class ContactCreateView(AdminRequiredMixin, CreateView):
    model = Contact
    template_name = 'fastfood/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts')

class ContactUpdateView(AdminRequiredMixin, UpdateView):
    model = Contact
    template_name = 'fastfood/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts')

class ContactDeleteView(AdminRequiredMixin, DeleteView):
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

class CategoryCreateView(AdminRequiredMixin, CreateView):
    model = Category
    template_name = 'fastfood/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(AdminRequiredMixin, UpdateView):
    model = Category
    template_name = 'fastfood/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(AdminRequiredMixin, DeleteView):
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
        context['categories'] = Category.objects.all()
        category_id = self.kwargs.get('category_id')
        if category_id:
            context['current_category'] = get_object_or_404(Category, pk=category_id)
        return context

class DishDetailView(DetailView):
    model = Dish
    template_name = 'fastfood/dish_detail.html'
    context_object_name = 'dish'

class DishCreateView(AdminRequiredMixin, CreateView):
    model = Dish
    template_name = 'fastfood/dish_form.html'
    form_class = DishForm
    success_url = reverse_lazy('dish_list')

class DishUpdateView(AdminRequiredMixin, UpdateView):
    model = Dish
    template_name = 'fastfood/dish_form.html'
    form_class = DishForm
    success_url = reverse_lazy('dish_list')

class DishDeleteView(AdminRequiredMixin, DeleteView):
    model = Dish
    template_name = 'fastfood/dish_confirm_delete.html'
    success_url = reverse_lazy('dish_list')

class PromotionListView(ListView):
    model = Promotion
    template_name = 'fastfood/promotion_list.html'
    context_object_name = 'promotions'

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'fastfood/promotion_detail.html'
    context_object_name = 'promotion'

class PromotionCreateView(AdminRequiredMixin, CreateView):
    model = Promotion
    template_name = 'fastfood/promotion_form.html'
    form_class = PromotionForm
    success_url = reverse_lazy('promotion_list')

class PromotionUpdateView(AdminRequiredMixin, UpdateView):
    model = Promotion
    template_name = 'fastfood/promotion_form.html'
    form_class = PromotionForm
    success_url = reverse_lazy('promotion_list')

class PromotionDeleteView(AdminRequiredMixin, DeleteView):
    model = Promotion
    template_name = 'fastfood/promotion_confirm_delete.html'
    success_url = reverse_lazy('promotion_list')

class OrderListView(AdminRequiredMixin, ListView):
    model = Order
    template_name = 'fastfood/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(AdminRequiredMixin, DetailView):
    model = Order
    template_name = 'fastfood/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(AdminRequiredMixin, CreateView):
    model = Order
    template_name = 'fastfood/order_form.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

class OrderUpdateView(AdminRequiredMixin, UpdateView):
    model = Order
    template_name = 'fastfood/order_form.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

class OrderDeleteView(AdminRequiredMixin, DeleteView):
    model = Order
    template_name = 'fastfood/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

class DeliveryView(LoginRequiredMixin, ListView):
    model = Delivery
    template_name = 'fastfood/delivery.html'
    context_object_name = 'deliveries'

    def get_queryset(self):
        return Delivery.objects.filter(order__user=self.request.user, order__delivery_type='courier')

class UserLoginView(LoginView):
    template_name = 'fastfood/login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class RegisterView(CreateView):
    template_name = 'fastfood/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = UserProfileForm()
        return context

    def form_valid(self, form):
        profile_form = UserProfileForm(self.request.POST)
        if profile_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            clients_group = Group.objects.get_or_create(name='Clients')[0]
            user.groups.add(clients_group)
            login(self.request, user)
            return redirect(self.success_url)
        else:
            self.object = None
            return self.form_invalid(form)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'fastfood/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            profile = UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(
                user=self.request.user,
                last_name='',
                first_name='',
                phone='',
                address=''
            )
        context['profile'] = profile
        return context

class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'fastfood/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)