from django import forms
from .models import Contact, Category, Dish, Promotion, Order
import re

class ContactForm(forms.ModelForm):
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\+7\s?\(\d{3}\)\s?\d{3}-\d{2}-\d{2}$', phone):
            raise forms.ValidationError('Формат телефона: +7 (XXX) XXX-XX-XX')
        return phone
    
    class Meta:
        model = Contact
        fields = ['address', 'phone', 'email']
        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите адрес (город, улица, дом)'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': '+7 (XXX) XXX-XX-XX',
                'type': 'tel'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'example@vkusno.ru'
            }),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите название категории'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'rows': 4,
                'placeholder': 'Введите описание категории'
            }),
        }

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'category', 'price', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите название блюда'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите цену',
                'step': '0.01',
                'min': '0'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'rows': 4,
                'placeholder': 'Введите описание блюда'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600'
            }),
        }

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['title', 'description', 'image', 'start_date', 'end_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите название акции'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'rows': 4,
                'placeholder': 'Введите описание акции'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'type': 'date'
            }),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'address', 'total_price']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите имя клиента'
            }),
            'address': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите адрес доставки'
            }),
            'total_price': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите общую стоимость',
                'step': '0.01',
                'min': '0'
            }),
        }