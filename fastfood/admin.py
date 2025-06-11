from django.contrib import admin
from .models import Contact, Category, Dish, Promotion, Order, DeliveryInfo

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
    list_display = ('id', 'customer_name', 'address', 'created_at')
    search_fields = ('customer_name', 'address')
    list_filter = ('created_at',)
    fields = ('customer_name', 'address', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(DeliveryInfo)
class DeliveryInfoAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    fields = ('description',)