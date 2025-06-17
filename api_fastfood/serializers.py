from rest_framework import serializers
from fastfood.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]

class DishSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    class Meta:
        model = Dish
        fields = [
            'name',
            'description',
            'price',
            'image',
            'category'
        ]

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = [
            'title',
            'description',
            'image',
            'start_date',
            'end_date'
        ]

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'address',
            'phone',
            'email'
        ]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user',
            'last_name',
            'first_name',
            'patronymic',
            'phone',
            'address',
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'user',
            'last_name',
            'first_name',
            'patronymic',
            'phone',
            'email',
            'address',
            'total_price',
            'delivery_type',
            'created_at'
        ]

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'order',
            'dish',
            'quantity'
        ]

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = [
            'order',
            'status',
            'courier_info',
            'estimated_time'
        ]