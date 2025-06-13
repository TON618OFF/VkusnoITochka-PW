from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Contact, Category, Dish, Promotion, Order, UserProfile
import re

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
        'placeholder': 'Введите пароль'
    }))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
        'placeholder': 'Подтвердите пароль'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите логин'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите email'
            }),
        }
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Логин уже занят.')
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email уже зарегистрирован.')
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают.')
        return cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['last_name', 'first_name', 'patronymic', 'phone', 'address']
        widgets = {
            'last_name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите фамилию'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите имя'
            }),
            'patronymic': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите отчество (необязательно)'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': '+7 (XXX) XXX-XX-XX',
                'type': 'tel'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'rows': 3,
                'placeholder': 'Введите адрес'
            }),
        }
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\+7\s?\(\d{3}\)\s?\d{3}-\d{2}-\d{2}$', phone):
            raise forms.ValidationError('Формат телефона: +7 (XXX) XXX-XX-XX')
        return phone

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
        'placeholder': 'Введите логин'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
        'placeholder': 'Введите пароль'
    }))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['address', 'phone', 'email']
        widgets = {
            'address': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'rows': 3,
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

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\+7\s?\(\d{3}\)\s?\d{3}-\d{2}-\d{2}$', phone):
            raise forms.ValidationError('Формат телефона: +7 (XXX) XXX-XX-XX')
        return phone

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
        fields = ['last_name', 'first_name', 'patronymic', 'phone', 'email', 'address', 'delivery_type']
        widgets = {
            'last_name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите фамилию'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите имя'
            }),
            'patronymic': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите отчество (необязательно)'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': '+7 (XXX) XXX-XX-XX',
                'type': 'tel'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'placeholder': 'Введите email'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600',
                'rows': 3,
                'placeholder': 'Введите адрес доставки'
            }),
            'delivery_type': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:border-red-600'
            }),
        }
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\+7\s?\(\d{3}\)\s?\d{3}-\d{2}-\d{2}$', phone):
            raise forms.ValidationError('Формат телефона: +7 (XXX) XXX-XX-XX')
        return phone