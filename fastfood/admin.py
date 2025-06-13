from django.contrib import admin
from .models import Contact, Category, Dish, Promotion, Order, OrderItem, Delivery, UserProfile

# Настройка заголовков админ-панели
admin.site.site_header = 'Вкусно - и точка: Админ-панель'
admin.site.site_title = 'Вкусно - и точка'
admin.site.index_title = 'Добро пожаловать в админ-панель Вкусно - и точка'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')
    search_fields = ('address', 'email')
    fields = ('address', 'phone', 'email')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    fields = ('name', 'description')

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'description')
    list_filter = ('category',)
    fields = ('name', 'description', 'price', 'image', 'category')

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    list_filter = ('start_date', 'end_date')
    fields = ('title', 'description', 'start_date', 'end_date', 'image')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'delivery_type', 'created_at')
    search_fields = ('last_name', 'first_name', 'email')
    list_filter = ('created_at', 'delivery_type')
    fields = ('user', 'last_name', 'first_name', 'patronymic', 'phone', 'email', 'address', 'total_price', 'delivery_type', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'dish', 'quantity')
    search_fields = ('order__id', 'dish__name')

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'estimated_time')
    search_fields = ('order__id',)
    fields = ('order', 'status', 'courier_info', 'estimated_time')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_name', 'first_name', 'phone')
    search_fields = ('user__username', 'last_name', 'first_name')
    fields = ('user', 'last_name', 'first_name', 'patronymic', 'phone', 'address')